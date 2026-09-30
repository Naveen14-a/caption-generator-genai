"""Gemini-powered personalized learning paths."""
from qna import generate_ai_text


def generate_learning_path(topic: str) -> str:
    topic = (topic or "").strip()
    if not topic:
        raise ValueError("Please provide a learning-path topic.")
    prompt = (
        "Design a practical, student-friendly learning path for the topic below. Organize it with "
        "exactly these sections: 1. Beginner concepts, 2. Intermediate concepts, 3. Advanced concepts, "
        "4. Recommended learning order. Include short descriptions, suggested practice, and realistic "
        "milestones. Adapt the plan for a learner starting with limited background.\n\nTopic: " + topic
    )
    return generate_ai_text(prompt)
