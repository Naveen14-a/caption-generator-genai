"""Gemini-powered personalized learning paths."""
from qna import generate_gemini_text


def generate_learning_path(topic: str) -> str:
    topic = (topic or "").strip()
    if not topic:
        raise ValueError("Please provide a learning-path topic.")
    return generate_gemini_text(
        f"Create a practical learning path for the topic below. Use these exact headings: Beginner concepts, Intermediate concepts, Advanced concepts, Recommended learning order. Add short practice ideas and realistic milestones. Assume the learner is starting with limited background.\n\nTopic: {topic}",
        system_instruction="You are EduGenie, a thoughtful curriculum designer. Sequence concepts from foundations to confident application.",
    )
