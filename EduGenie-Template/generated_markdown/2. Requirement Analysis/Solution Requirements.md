# Solution Requirements

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| FR-01 | Serve the EduGenie homepage | Must | GET `/` returns rendered `index.html` |
| FR-02 | Explain a concept locally | Must | `/explain` uses LaMini-Flan-T5 Seq2Seq generation |
| FR-03 | Answer student questions | Must | `/ask` returns a Gemini-generated answer |
| FR-04 | Generate a quiz | Must | `/quiz` validates five questions and four options |
| FR-05 | Summarize text | Must | `/summarize` returns a student-friendly summary |
| FR-06 | Generate a learning path | Must | `/learning-path` includes four required sections |
| FR-07 | Handle empty input | Must | Useful validation error is returned |
| FR-08 | Handle API/model errors | Must | Safe response without secret exposure |
| FR-09 | Use asynchronous UI requests | Should | Fetch updates result cards without reload |
| FR-10 | Support responsive UI | Should | Layout works on desktop and mobile |


## Non-Functional Requirements

- Python 3.10+ compatible.
- Modular beginner-readable code.
- Cached local model loading.
- Environment-based configuration.
- Responsive, accessible, and reduced-motion-aware UI.
