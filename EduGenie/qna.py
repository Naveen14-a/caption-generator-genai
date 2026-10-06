"""Shared Google Gemini client with retries and automatic model fallback."""
import os
import time
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().with_name(".env"))
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def gemini_configured() -> bool:
    key = os.getenv("GEMINI_API_KEY", "").strip()
    return bool(key and not key.startswith(("YOUR_", "your_")))


@lru_cache(maxsize=1)
def _get_client():
    if not gemini_configured():
        raise RuntimeError("Gemini API key is not configured. Add GEMINI_API_KEY to .env.")
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError("The Google Gen AI SDK is not installed. Run pip install -r requirements.txt.") from exc
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"].strip())


def _is_temporary_error(exc: Exception) -> bool:
    text = str(exc).upper()
    return any(code in text for code in ("429", "500", "502", "503", "504", "UNAVAILABLE", "RESOURCE_EXHAUSTED", "OVERLOADED"))


def _normalise_model(name: str) -> str:
    return name.removeprefix("models/").strip()


@lru_cache(maxsize=1)
def _model_candidates() -> tuple[str, ...]:
    """Return configured model first, then a fallback, then models exposed to this key."""
    candidates = []
    for value in (DEFAULT_MODEL, os.getenv("GEMINI_FALLBACK_MODEL", "").strip()):
        if value and value not in candidates:
            candidates.append(_normalise_model(value))
    try:
        models = _get_client().models.list()
        discovered = []
        for model in models:
            name = _normalise_model(getattr(model, "name", ""))
            actions = getattr(model, "supported_actions", None) or []
            if name and "generateContent" in actions and name not in candidates:
                discovered.append(name)
        # Prefer lightweight/flash models for a responsive student app.
        discovered.sort(key=lambda name: ("flash" not in name.lower(), len(name)))
        candidates.extend(discovered[:5])
    except Exception:
        # The configured model remains usable even if model discovery is unavailable.
        pass
    return tuple(candidates)


def _generate(prompt: str, *, system_instruction: str, json_mode: bool) -> str:
    from google.genai import types

    last_error = None
    for model in _model_candidates():
        for attempt in range(2):
            try:
                config = types.GenerateContentConfig(
                    temperature=0.25 if json_mode else 0.45,
                    max_output_tokens=2200 if json_mode else 1800,
                    system_instruction=system_instruction,
                    **({"response_mime_type": "application/json"} if json_mode else {}),
                )
                response = _get_client().models.generate_content(
                    model=model,
                    contents=prompt,
                    config=config,
                )
                text = getattr(response, "text", None)
                if not text or not text.strip():
                    raise RuntimeError("Gemini returned an empty response.")
                return text.strip()
            except RuntimeError:
                raise
            except Exception as exc:
                last_error = exc
                if _is_temporary_error(exc) and attempt == 0:
                    time.sleep(2)
                    continue
                # Try the next model for overload, quota, and model-availability errors.
                break

    if last_error and _is_temporary_error(last_error):
        raise RuntimeError("Gemini models are temporarily busy or rate-limited. Please retry in a moment.") from last_error
    raise RuntimeError("Gemini could not generate a response. Check the API key, model access, quota, and network connection.") from last_error


def generate_gemini_text(prompt: str, *, system_instruction: str | None = None) -> str:
    return _generate(
        prompt,
        system_instruction=system_instruction or "You are EduGenie, a precise and encouraging educational tutor.",
        json_mode=False,
    )


def generate_gemini_json(prompt: str, *, system_instruction: str | None = None) -> str:
    return _generate(
        prompt,
        system_instruction=system_instruction or "Return only valid JSON. Do not include markdown fences.",
        json_mode=True,
    )


def answer_question(question: str) -> str:
    question = (question or "").strip()
    if not question:
        raise ValueError("Please provide a question.")
    return generate_gemini_text(
        f"Answer this student question clearly and accurately. Define unfamiliar terms, explain the reasoning briefly, and include one simple example when useful.\n\nStudent question:\n{question}",
        system_instruction="You are EduGenie, a patient tutor. Match the learner's level, avoid jargon overload, and be honest about uncertainty.",
    )
