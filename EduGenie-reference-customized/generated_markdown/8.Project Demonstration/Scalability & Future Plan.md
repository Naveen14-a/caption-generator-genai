# Scalability & Future Plan

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 1 Mark


## Current Limitations

| No. | Limitation | Impact | Priority |
|---|---|---|---|
| 1 | Local model is large | First explanation request needs disk/download | High |
| 2 | Gemini provider dependency | Cloud features depend on key/network/quota | High |
| 3 | No persistent progress data | No history or learner analytics | Medium |


## Scalability Plan

| Aspect | Current State | Proposed Upgrade |
|---|---|---|
| User load | Single FastAPI process | Production workers and autoscaling |
| Data storage | No database | PostgreSQL for profiles, history, progress |
| Performance | Cached local model, synchronous requests | Async jobs, queues, response caching |
| Security | `.env` key | Secret manager, authentication, rate limits, audit logs |


## Future Roadmap

| Phase | Enhancement | Impact |
|---|---|---|
| 2 | Voice and multilingual learning | Improved accessibility |
| 3 | Image/PDF question solving | Richer study inputs |
| 4 | Progress dashboard and gamification | Motivation and retention |
| 5 | Teacher/parent dashboards and LMS integration | Institutional adoption |
