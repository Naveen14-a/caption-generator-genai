import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__ ).resolve().with_name(".env"))

DEFAULT_MODEL = os.getenv("AI_MODEL", "openai/gpt-4o-mini")
DEFAULT_BASE_URL = os.getenv(
    "AI_BASE_URL",
    "https://openrouter.ai/api/v1",
 )


@lru_cache(maxsize=1)
def _get_client():
    api_key = os.getenv("AI_API_KEY", "").strip()

    if not api_key or api_key.startswith("YOUR_"):
        raise RuntimeError(
            "AI API key is not configured. Add AI_API_KEY to .env."
        )

    return OpenAI(
        api_key=api_key,
        base_url=DEFAULT_BASE_URL,
    )


def generate_ai_text(prompt: str) -> str:
    try:
        response = _get_client().chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are EduGenie, a helpful educational tutor.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.4,
        )
    except Exception as exc:
        raise RuntimeError(
            "The AI service could not generate a response. "
            "Check the API key, model, and network connection."
        ) from exc

    text = response.choices[0].message.content

    if not text:
        raise RuntimeError("The AI service returned an empty response.")

    return text.strip()


def answer_question(question: str) -> str:
    question = (question or "").strip()

    if not question:
        raise ValueError("Please provide a question.")

    prompt = (
        "Answer the student's question accurately and in simple, "
        "student-friendly language.\n\n"
        f"Student question: {question}"
    )

    return generate_ai_text(prompt)
