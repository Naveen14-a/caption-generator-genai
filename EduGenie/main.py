"""EduGenie FastAPI application powered by Google Gemini."""
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

from explanation_module import explain_concept
from learning_path import generate_learning_path
from qna import answer_question, gemini_configured
from quiz_module import generate_quiz
from summary_module import summarize_text

app = FastAPI(title="EduGenie", description="Gemini-powered learning assistant", version="2.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def _clean_input(value: str, field_name: str, max_length: int = 12000) -> str:
    value = (value or "").strip()
    if not value:
        raise ValueError(f"Please provide {field_name}.")
    if len(value) > max_length:
        raise ValueError(f"Please keep {field_name} under {max_length:,} characters.")
    return value


def _error_response(exc: Exception) -> JSONResponse:
    message = str(exc) or "The request could not be completed."
    lowered = message.lower()
    status = 503 if any(term in lowered for term in ("api key", "gemini", "quota", "model", "network")) else 400
    return JSONResponse(status_code=status, content={"error": message})


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health():
    return {"status": "ok", "gemini_configured": gemini_configured()}


@app.post("/explain")
async def explain(concept: str = Form("")):
    try:
        return {"result": explain_concept(_clean_input(concept, "a concept", 3000))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/ask")
async def ask(question: str = Form("")):
    try:
        return {"result": answer_question(_clean_input(question, "a question", 6000))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/quiz")
async def quiz(topic: str = Form("")):
    try:
        return {"result": generate_quiz(_clean_input(topic, "a quiz topic", 2000))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/summarize")
async def summarize(text: str = Form("")):
    try:
        return {"result": summarize_text(_clean_input(text, "text to summarize", 16000))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/learning-path")
async def learning_path(topic: str = Form("")):
    try:
        return {"result": generate_learning_path(_clean_input(topic, "a learning-path topic", 2000))}
    except Exception as exc:
        return _error_response(exc)


@app.exception_handler(Exception)
async def unexpected_error(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "An unexpected server error occurred."})
