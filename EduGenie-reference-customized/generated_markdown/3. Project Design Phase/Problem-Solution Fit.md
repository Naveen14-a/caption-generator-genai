# Problem-Solution Fit

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Problem

Students need an accessible study companion that can explain, answer, summarize, test, and guide them without switching applications.

## Solution

EduGenie combines a local model for concept explanation and Gemini for richer cloud-generated educational features in one FastAPI web application.

| User Pain | EduGenie Response | Evidence |
|---|---|---|
| Complex topics | Simple local explanation | LaMini prompt requests definition, example, takeaway |
| Unanswered doubts | Student Q&A | `answer_question(question)` |
| Passive revision | Five-question quiz | Validated JSON schema |
| Long passages | Concise summary | Gemini summary prompt |
| Unclear study order | Structured learning path | Beginner → intermediate → advanced |


## MVP Boundary

The current project intentionally avoids authentication, databases, payments, progress tracking, and external LMS integrations. Those belong in future iterations after the core learning workflow is validated.
