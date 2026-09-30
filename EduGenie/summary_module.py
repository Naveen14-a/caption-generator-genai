"""Gemini-powered student-friendly text summarization."""
from qna import generate_ai_text


def summarize_text(text: str) -> str:
    text = (text or "").strip()
    if not text:
        raise ValueError("Please provide text to summarize.")
    prompt = (
        "Summarize the educational text below for a student. Preserve the main ideas, key facts, "
        "and important relationships; remove repetition and minor details. Use a clear heading and "
        "concise bullet points when helpful. Do not invent information.\n\nText:\n" + text
    )
    return generate_ai_text(prompt)
