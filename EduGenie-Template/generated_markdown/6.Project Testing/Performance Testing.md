# Performance Testing

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


## Testing Overview

| Field | Actual Details |
|---|---|
| Tool | Browser, FastAPI TestClient, curl, Uvicorn logs |
| Type | Functional smoke testing and startup verification |
| Target | `/`, `/explain`, `/ask`, `/quiz`, `/summarize`, `/learning-path` |
| Environment | Local sandbox and Windows-compatible commands |
| Date | 30 September 2026 |

## Test Scenarios

| No. | Scenario | Expected Outcome | Observed |
|---|---|---|---|
| 1 | GET `/` | HTML homepage, status 200 | Pass |
| 2 | POST `/explain` with gravity | LaMini explanation, status 200 | Pass |
| 3 | POST `/ask` with placeholder key | Safe configuration error | Pass |
| 4 | POST `/quiz` | Safe provider response or validated quiz | Pass |
| 5 | POST `/summarize` | Safe provider response or summary | Pass |
| 6 | POST `/learning-path` | Safe provider response or path | Pass |
| 7 | Empty input | Useful validation response | Pass |


## Results

| Metric | Target | Result | Status |
|---|---|---|---|
| Startup | Uvicorn starts | Application startup complete | Pass |
| Homepage | HTTP 200 | HTTP 200 | Pass |
| Static CSS | HTTP 200 | HTTP 200 | Pass |
| Local explanation | Valid response | Valid LaMini response | Pass |
| Gemini configuration | No secret leakage | Safe 503 message when absent | Pass |
| Error handling | Useful errors | JSON error responses | Pass |

The first local LaMini request downloads model weights and may require several GB of disk space. Cloud Gemini features depend on a valid key, model availability, and network access.
