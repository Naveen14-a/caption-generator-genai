# No. of Functional Features Included in the Solution

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Functional Features Overview

| No. | Feature | Description | Module | Status | Contribution |
|---|---|---|---|---|---|
| 1 | Concept Explanation | Student-friendly local explanation | explanation_module.py | Done | Core |
| 2 | Student Q&A | Gemini answer with reasoning | qna.py | Done | Core |
| 3 | Quiz Generation | Five MCQs with four options | quiz_module.py | Done | Core |
| 4 | Text Summarization | Clear revision summary | summary_module.py | Done | Core |
| 5 | Learning Path | Beginner/intermediate/advanced order | learning_path.py | Done | Core |
| 6 | Responsive dashboard | Animated cards, theme and focus modes | index.html/style.css | Done | Additional |
| 7 | Safe error handling | Validation and provider/model errors | main.py | Done | Additional |


## Feature Summary

| Metric | Value |
|---|---:|
| Total features planned | 7 |
| Total features implemented | 7 |
| Core features | 5 |
| Additional features | 2 |
| Features tested and verified | 7 |

## Category Breakdown

| Category | Features |
|---|---|
| UI | Responsive cards, theme toggle, focus mode, quick prompts |
| Backend | Five FastAPI routes and input validation |
| Local AI | LaMini-Flan-T5 Seq2Seq explanation |
| API integration | Gemini Q&A, quiz, summary, learning path |
| Security/configuration | `.env` key loading and safe error messages |
