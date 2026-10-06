"""Gemini-powered concept explanations."""
from qna import generate_gemini_text


def explain_concept(concept: str) -> str:
    concept = (concept or "").strip()
    if not concept:
        raise ValueError("Please provide a concept.")
    return generate_gemini_text(
        f"Explain the concept below for a student. Use these exact headings: Quick idea, How it works, Real-world example, Remember this. Keep it clear and concise.\n\nConcept: {concept}",
        system_instruction="You are EduGenie, an engaging science and learning tutor. Use plain language and accurate examples.",
    )
