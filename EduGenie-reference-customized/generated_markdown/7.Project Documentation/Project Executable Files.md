# Project Executable Files

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 3 Marks


## Submission Checklist

| No. | Item | Submitted |
|---|---|---|
| 1 | Complete source code | Yes - EduGenie project |
| 2 | README / setup guide | Yes |
| 3 | requirements.txt | Yes |
| 4 | Database schema | N/A - no database |
| 5 | .env.example | Recommended - never commit key |
| 6 | Deployed URL | To be added by team |
| 7 | APK/executable | N/A - web app |
| 8 | Dockerfile | Optional |
| 9 | Tests/results | Yes - documented |
| 10 | Demo video | To be added by team |


## Actual File Structure

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

## Run Instructions

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Known Limitations

- Gemini features require a valid `GEMINI_API_KEY`.
- The local LaMini model requires significant disk space on first download.
- No authentication, saved history, or progress database in the MVP.
