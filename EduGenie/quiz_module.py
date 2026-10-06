"""Gemini-powered five-question multiple-choice quiz generation."""
import json

from qna import generate_gemini_json


def _validate_quiz(data):
    questions = data.get("questions") if isinstance(data, dict) else data
    if not isinstance(questions, list) or len(questions) != 5:
        raise ValueError("Gemini returned a quiz that did not contain exactly five questions.")
    result = []
    for index, item in enumerate(questions, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Quiz question {index} was malformed.")
        options = item.get("options")
        answer = item.get("correct_answer")
        question = str(item.get("question", "")).strip()
        if not question or not isinstance(options, list) or len(options) != 4 or not answer:
            raise ValueError(f"Quiz question {index} must have a question, four options, and a correct answer.")
        options = [str(option).strip() for option in options]
        if str(answer).strip() not in options:
            raise ValueError(f"Quiz question {index} has an answer that is not one of its options.")
        result.append({"question": question, "options": options, "correct_answer": str(answer).strip()})
    return {"questions": result}


def generate_quiz(topic: str):
    topic = (topic or "").strip()
    if not topic:
        raise ValueError("Please provide a quiz topic.")
    raw = generate_gemini_json(
        "Create exactly five student-friendly multiple-choice questions about this topic. Return JSON only with this shape: "
        '{"questions":[{"question":"...","options":["...","...","...","..."],"correct_answer":"..."}]}\n\n'
        f"Topic: {topic}",
        system_instruction="You create fair educational quizzes. Every correct_answer must exactly match one option.",
    )
    try:
        return _validate_quiz(json.loads(raw))
    except json.JSONDecodeError as exc:
        raise ValueError("Gemini returned quiz content that was not valid JSON.") from exc
