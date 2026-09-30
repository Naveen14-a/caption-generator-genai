"""Local concept explanations using MBZUAI/LaMini-Flan-T5-783M."""
from functools import lru_cache

MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"


@lru_cache(maxsize=1)
def _load_model():
    try:
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError("The local explanation dependencies are not installed.") from exc

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


def explain_concept(concept: str) -> str:
    """Explain a concept with a cached T5/Seq2Seq model."""
    concept = (concept or "").strip()
    if not concept:
        raise ValueError("Please provide a concept.")

    tokenizer, model = _load_model()
    prompt = (
        "Explain the following concept to a student in clear, simple language. "
        "Use a short definition, an intuitive example, and one key takeaway.\n\n"
        f"Concept: {concept}"
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    output_ids = model.generate(
        **inputs,
        max_new_tokens=180,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3,
    )
    answer = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
    if not answer:
        raise RuntimeError("The local explanation model returned no answer.")
    return answer
