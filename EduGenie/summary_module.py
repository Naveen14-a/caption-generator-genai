"""Gemini-powered student-friendly text summarization."""
from qna import generate_gemini_text


def summarize_text(text: str) -> str:
    text = (text or "").strip()
    if not text:
        raise ValueError("Please provide text to summarize.")
    return generate_gemini_text(
        f"Summarize the educational passage below. Use these headings: Main idea, Key points, One-line takeaway. Preserve important facts, remove repetition, and do not invent information.\n\nPassage:\n{text}",
        system_instruction="You are EduGenie, a revision coach. Make summaries concise, accurate, and easy to scan.",
    )
