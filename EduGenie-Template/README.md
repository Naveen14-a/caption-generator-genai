# EduGenie – Google Gemini Powered Learning Assistant

Project documentation deliverables for **Team SWTID-2026-3656**.

## Project summary

EduGenie is a FastAPI-based educational AI web application with five features: Concept Explanation, Student Q&A, Quiz Generation, Text Summarization, and Personalized Learning Path. It uses the local `MBZUAI/LaMini-Flan-T5-783M` Seq2Seq model for concept explanation and Google Gemini through the current `google-genai` SDK for the other four features.

## Actual project structure

```text
EduGenie/
├── main.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── templates/index.html
└── static/style.css
```

## Reference-template phases completed

1. Brainstorming & Ideation
2. Requirement Analysis
3. Project Design Phase
4. Project Planning Phase
5. Project Development Phase
6. Project Testing
7. Project Documentation
8. Project Demonstration

All 22 reference PDF deliverables were customized to match the actual EduGenie source files, route names, modules, model choices, dependencies, UI, and testing results.

## Local run command

```powershell
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Environment configuration

```env
GEMINI_API_KEY=your_google_gemini_key
GEMINI_MODEL=gemini-2.5-flash
```

Never commit a real API key. Add `.env` to `.gitignore` and use a secret manager/environment settings for deployment.

## Important evaluator notes

- The local concept model may need several GB of disk space during its first download.
- Gemini features require a valid API key and network access.
- The current MVP has no database, authentication, saved history, or progress dashboard.
- Replace generic `Team Member 1` labels with the actual member names before submission.
- Add the final project repository URL, deployed URL, and demo video link where marked.

## Source of truth

The documentation was generated from the EduGenie project files in the accompanying project folder, including `main.py`, `qna.py`, `explanation_module.py`, `quiz_module.py`, `summary_module.py`, `learning_path.py`, `requirements.txt`, `templates/index.html`, and `static/style.css`.
