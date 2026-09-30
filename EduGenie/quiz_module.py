"""Gemini-powered five-question multiple-choice quiz generation."""
import json
import re

from qna import generate_ai_text


def _extract_json(text: str):
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"(\[.*\]|\{.*\})", cleaned, flags=re.DOTALL)
        if not match:
            raise ValueError("Gemini returned quiz content that was not valid JSON.")
        return json.loads(match.group(1))


def _validate_quiz(data):
    questions = data.get("questions") if isinstance(data, dict) else data
    if not isinstance(questions, list) or len(questions) != 5:
        raise ValueError("Gemini returned a quiz that did not contain exactly five questions.")
    result = []
    for index, item in enumerate(questions, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Quiz question {index} was malformed.")
        options = item.get("options")
        answer = item.get("correct_answer", item.get("answer"))
        if not isinstance(options, list) or len(options) != 4 or not answer:
            raise ValueError(f"Quiz question {index} must have four options and a correct answer.")
        result.append({"question": str(item.get("question", "")), "options": [str(x) for x in options], "correct_answer": str(answer)})
    return {"questions": result}


def generate_quiz(topic: str):
    topic = (topic or "").strip()
    if not topic:
        raise ValueError("Please provide a quiz topic.")
    prompt = (
        "Create exactly five educational multiple-choice questions about the topic below. "
        "Each question must have exactly four options and a correct_answer matching one option. "
        "Return JSON only in this shape: {\"questions\":[{\"question\":\"...\",\"options\":[\"...\",\"...\",\"...\",\"...\"],\"correct_answer\":\"...\"}]}. "
        "Keep the difficulty suitable for a general student.\n\nTopic: " + topic
    )
    return _validate_quiz(_extract_json(generate_ai_text(prompt)))
