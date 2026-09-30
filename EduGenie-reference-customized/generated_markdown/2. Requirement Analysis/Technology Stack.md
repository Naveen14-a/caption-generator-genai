# Technology Stack

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


| Layer | Technology | Actual Use in EduGenie |
|---|---|---|
| Backend | Python + FastAPI | Application, routing, form handling, JSON responses |
| Server | Uvicorn | Runs the ASGI application locally/deployed |
| Templates | Jinja2 | Renders `templates/index.html` |
| Frontend | HTML, CSS, JavaScript | Responsive animated learning dashboard |
| Cloud AI | Google Gemini via `google-genai` | Q&A, quiz, summarization, learning path |
| Local AI | Transformers + PyTorch | LaMini-Flan-T5 concept explanation |
| Tokenizer | SentencePiece | Supports the T5 tokenizer |
| Configuration | python-dotenv | Loads `.env` before AI modules read the key |
| Form parsing | python-multipart | Supports FastAPI form data |


## Environment

```env
GEMINI_API_KEY=your_google_gemini_key
GEMINI_MODEL=gemini-2.5-flash
```
