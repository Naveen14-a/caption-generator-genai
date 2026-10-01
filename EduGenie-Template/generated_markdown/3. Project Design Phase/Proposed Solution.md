# Proposed Solution

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Project Overview

**Objective:** Provide a simple AI-powered learning assistant for students.  
**Scope:** Five focused learning tools in one responsive browser interface.  
**Core design:** FastAPI routes call modular Python functions; the frontend uses `fetch()` to update results in place.

## Feature Workflow

1. Student chooses a card.
2. Student enters a concept, question, topic, or passage.
3. Frontend posts form data to the matching endpoint.
4. Backend validates input.
5. Local or Gemini model generates content.
6. Frontend displays the result and error states safely.

## Key Design Decisions

- Use `AutoModelForSeq2SeqLM`, not `pipeline("text-generation")`, for the T5 model.
- Cache the local model with `lru_cache`.
- Load `.env` before importing modules that inspect the key.
- Validate quiz JSON before displaying it.
- Keep the frontend framework-free for easy evaluation.
