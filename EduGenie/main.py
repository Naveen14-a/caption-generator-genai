"""EduGenie FastAPI application."""
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Load .env before importing modules that may inspect GEMINI_API_KEY.
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

from explanation_module import explain_concept
from learning_path import generate_learning_path
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

app = FastAPI(title="EduGenie", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def _clean_input(value: str, field_name: str) -> str:
    value = (value or "").strip()
    if not value:
        raise ValueError(f"Please provide {field_name}.")
    return value


def _error_response(exc: Exception) -> JSONResponse:
    message = str(exc) or "The request could not be completed."
    lowered = message.lower()
    status = 503 if any(term in lowered for term in ("api key", "gemini", "model")) else 400
    return JSONResponse(status_code=status, content={"error": message})


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/explain")
async def explain(concept: str = Form(...)):
    try:
        return {"result": explain_concept(_clean_input(concept, "a concept"))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/ask")
async def ask(question: str = Form(...)):
    try:
        return {"result": answer_question(_clean_input(question, "a question"))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/quiz")
async def quiz(topic: str = Form(...)):
    try:
        return {"result": generate_quiz(_clean_input(topic, "a quiz topic"))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        return {"result": summarize_text(_clean_input(text, "text to summarize"))}
    except Exception as exc:
        return _error_response(exc)


@app.post("/learning-path")
async def learning_path(topic: str = Form(...)):
    try:
        return {"result": generate_learning_path(_clean_input(topic, "a learning-path topic"))}
    except Exception as exc:
        return _error_response(exc)


@app.exception_handler(Exception)
async def unexpected_error(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "An unexpected server error occurred."})
