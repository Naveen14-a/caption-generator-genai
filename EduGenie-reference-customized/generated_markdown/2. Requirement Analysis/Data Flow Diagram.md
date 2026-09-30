# Data Flow Diagram

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Context Flow

```text
[Student Browser]
       | HTML form data
       v
[FastAPI + Jinja2 Application]
       | /explain uses local Seq2Seq model
       | /ask, /quiz, /summarize, /learning-path use Gemini
       v
[LaMini-Flan-T5] or [Google Gemini API]
       | generated educational response
       v
[JSON response rendered in browser]
```

## Request Flow

1. User enters a value in a feature card.
2. JavaScript sends a `fetch()` POST request as `FormData`.
3. FastAPI validates and cleans the field.
4. The selected module generates a response.
5. Backend returns `{ "result": ... }` or `{ "error": ... }`.
6. Frontend renders the response without a page reload.

## Data and Security

The MVP has no database. User input is processed in memory. `GEMINI_API_KEY` is loaded from `.env`, never hard-coded in Python, and never sent to the browser.
