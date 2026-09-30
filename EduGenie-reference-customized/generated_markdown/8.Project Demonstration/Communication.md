# Communication

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 1 Mark


## Communication Plan

| No. | Type | Frequency | Channel | Participants | Purpose |
|---|---|---|---|---|---|
| 1 | Team standup | Daily | Chat/call | All members | Share progress and blockers |
| 2 | Progress update | Weekly | Shared document | All members | Review phase deliverables |
| 3 | Bug discussion | As needed | Chat/Git issue | Developer/reviewer | Resolve errors |
| 4 | Stakeholder review | Bi-weekly | Demo call | Team/mentor | Collect feedback |
| 5 | Final rehearsal | Once | Browser walkthrough | All members | Practice evaluation flow |


## Challenges and Resolutions

| No. | Challenge | Resolution |
|---|---|---|
| 1 | T5 model was initially at risk of using the wrong pipeline | Implemented AutoModelForSeq2SeqLM and model.generate |
| 2 | Environment key load order | Loaded `.env` before importing feature modules |
| 3 | Gemini key missing | Returned safe user-facing 503 response |
| 4 | Large local model download | Cached model and documented disk requirement |
