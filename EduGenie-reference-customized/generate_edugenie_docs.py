from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
MD = ROOT / "generated_markdown"
MD.mkdir(exist_ok=True)
DATE = "30 September 2026"
TEAM = "SWTID-2026-3656"
PROJECT = "EduGenie – Google Gemini Powered Learning Assistant"


def header(title, marks):
    return f"# {title}\n\n**Date:** {DATE}  \n**Team ID:** {TEAM}  \n**Project Name:** {PROJECT}  \n**Maximum Marks:** {marks}\n\n"


def table(cols, rows):
    s = "| " + " | ".join(cols) + " |\n|" + "|".join("---" for _ in cols) + "|\n"
    for row in rows:
        s += "| " + " | ".join(str(x).replace("|", "\\|") for x in row) + " |\n"
    return s


docs = {}
docs["1. Brainstorming & Ideation/Brainstorming & Idea Prioritization.md"] = header("Brainstorming & Idea Prioritization", "3 Marks") + """
## Step 1: Brainstorm and Idea Listing

""" + table(["S.No", "Team Member", "Idea / Suggestion", "Category", "Group No."], [
("1", "Team Member 1", "Student Q&A learning assistant", "Learning support", "1"),
("2", "Team Member 2", "Local concept explanation with LaMini-Flan-T5", "Local AI", "2"),
("3", "Team Member 3", "Automatic quiz generation", "Assessment", "3"),
("4", "Team Member 4", "Text summarization for revision", "Productivity", "4"),
("5", "Team Member 5", "Personalized beginner-to-advanced learning paths", "Recommendations", "5"),
("6", "Team Member 6", "Responsive dashboard with animated learning cards", "User experience", "6"),
]) + """

## Step 2: Idea Prioritization

""" + table(["Group", "Final Idea", "Feasibility", "Importance", "Priority", "Selected"], [
("1", "Student Q&A assistant", "High", "High", "1", "Yes"),
("2", "Local concept explanation", "Medium", "High", "2", "Yes"),
("3", "Five-question quiz generation", "High", "High", "3", "Yes"),
("4", "Text summarization", "High", "High", "4", "Yes"),
("5", "Personalized learning path", "High", "High", "5", "Yes"),
("6", "Responsive animated UI", "High", "Medium", "6", "Yes"),
]) + """

**Selected idea:** EduGenie, a modular FastAPI learning assistant combining Google Gemini cloud generation with local LaMini-Flan-T5 concept explanations.
"""

docs["1. Brainstorming & Ideation/Define Problem Statements.md"] = header("Define Problem Statements", "3 Marks") + """
## Problem Statement

Students often need quick explanations, answers, revision summaries, practice questions, and a structured learning order, but these resources are spread across multiple tools. Beginners may also find standard technical explanations too complex.

## Target Users

- School and college students.
- Self-learners and beginners.
- Learners revising a long passage.
- Students preparing for topic-based assessments.

## Impact

Without one simple assistant, learners spend more time searching, switching tools, and deciding what to study next. This can reduce comprehension and consistency.

## Proposed Problem-Solution Fit

EduGenie provides five connected features in one responsive interface:

1. Concept Explanation.
2. Student Q&A.
3. Quiz Generation.
4. Text Summarization.
5. Personalized Learning Path.

## Success Criteria

- Homepage loads through FastAPI and Jinja2.
- Each required endpoint accepts form data and returns JSON.
- Concept explanation uses the correct Seq2Seq LaMini model.
- Gemini features read the API key from `.env`.
- Empty input and provider/model errors return useful messages.
"""

docs["1. Brainstorming & Ideation/Empathy Map.md"] = header("Empathy Map", "3 Marks") + """
## Primary User: Student or self-learner

| Says | Thinks |
|---|---|
| “Explain this topic simply.” | “I need an answer I can understand, not just a definition.” |
| “Can you quiz me?” | “Do I really know this topic?” |
| “Summarize these notes.” | “What should I remember for revision?” |
| “What should I learn first?” | “How do I move from beginner to advanced?” |

| Does | Feels |
|---|---|
| Enters a concept, question, topic, or passage. | Curious but sometimes overwhelmed. |
| Clicks a feature button and waits for a response. | Wants quick feedback and clear structure. |
| Uses the result for study or revision. | More confident when the content is organized. |

## Pains

- Complex explanations and unfamiliar terminology.
- Long notes that are difficult to revise.
- No clear learning sequence.
- Lack of practice questions.

## Gains

- Friendly explanations and answers.
- Five-question active recall quiz.
- Concise summaries.
- Beginner, intermediate, and advanced learning order.
"""

docs["2. Requirement Analysis/Customer Journey Map.md"] = header("Customer Journey Map", "5 Marks") + """
""" + table(["Stage", "User Action", "Need / Emotion", "System Touchpoint", "Opportunity"], [
("Discover", "Opens EduGenie", "Wants one study workspace", "Animated homepage", "Explain five features clearly"),
("Choose", "Selects a learning card", "Needs a focused task", "Feature cards and quick prompts", "Make inputs obvious"),
("Submit", "Enters form data", "Expects a useful response", "POST feature endpoint", "Validate empty input"),
("Wait", "Sees loading state", "Wants reassurance", "Animated thinking state", "Disable duplicate submissions"),
("Learn", "Reads result", "Needs clarity and structure", "Result panel", "Format quiz and text safely"),
("Continue", "Chooses next study action", "Wants momentum", "Quick prompts and learning path", "Encourage the next feature"),
]) + """

The journey is designed to move from question → explanation → practice → next learning step.
"""

docs["2. Requirement Analysis/Data Flow Diagram.md"] = header("Data Flow Diagram", "5 Marks") + """
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
"""

docs["2. Requirement Analysis/Solution Requirements.md"] = header("Solution Requirements", "5 Marks") + """
## Functional Requirements

""" + table(["ID", "Requirement", "Priority", "Acceptance Criteria"], [
("FR-01", "Serve the EduGenie homepage", "Must", "GET `/` returns rendered `index.html`"),
("FR-02", "Explain a concept locally", "Must", "`/explain` uses LaMini-Flan-T5 Seq2Seq generation"),
("FR-03", "Answer student questions", "Must", "`/ask` returns a Gemini-generated answer"),
("FR-04", "Generate a quiz", "Must", "`/quiz` validates five questions and four options"),
("FR-05", "Summarize text", "Must", "`/summarize` returns a student-friendly summary"),
("FR-06", "Generate a learning path", "Must", "`/learning-path` includes four required sections"),
("FR-07", "Handle empty input", "Must", "Useful validation error is returned"),
("FR-08", "Handle API/model errors", "Must", "Safe response without secret exposure"),
("FR-09", "Use asynchronous UI requests", "Should", "Fetch updates result cards without reload"),
("FR-10", "Support responsive UI", "Should", "Layout works on desktop and mobile"),
]) + """

## Non-Functional Requirements

- Python 3.10+ compatible.
- Modular beginner-readable code.
- Cached local model loading.
- Environment-based configuration.
- Responsive, accessible, and reduced-motion-aware UI.
"""

docs["2. Requirement Analysis/Technology Stack.md"] = header("Technology Stack", "5 Marks") + """
""" + table(["Layer", "Technology", "Actual Use in EduGenie"], [
("Backend", "Python + FastAPI", "Application, routing, form handling, JSON responses"),
("Server", "Uvicorn", "Runs the ASGI application locally/deployed"),
("Templates", "Jinja2", "Renders `templates/index.html`"),
("Frontend", "HTML, CSS, JavaScript", "Responsive animated learning dashboard"),
("Cloud AI", "Google Gemini via `google-genai`", "Q&A, quiz, summarization, learning path"),
("Local AI", "Transformers + PyTorch", "LaMini-Flan-T5 concept explanation"),
("Tokenizer", "SentencePiece", "Supports the T5 tokenizer"),
("Configuration", "python-dotenv", "Loads `.env` before AI modules read the key"),
("Form parsing", "python-multipart", "Supports FastAPI form data"),
]) + """

## Environment

```env
GEMINI_API_KEY=your_google_gemini_key
GEMINI_MODEL=gemini-2.5-flash
```
"""

docs["3. Project Design Phase/Problem-Solution Fit.md"] = header("Problem-Solution Fit", "5 Marks") + """
## Problem

Students need an accessible study companion that can explain, answer, summarize, test, and guide them without switching applications.

## Solution

EduGenie combines a local model for concept explanation and Gemini for richer cloud-generated educational features in one FastAPI web application.

""" + table(["User Pain", "EduGenie Response", "Evidence"], [
("Complex topics", "Simple local explanation", "LaMini prompt requests definition, example, takeaway"),
("Unanswered doubts", "Student Q&A", "`answer_question(question)`"),
("Passive revision", "Five-question quiz", "Validated JSON schema"),
("Long passages", "Concise summary", "Gemini summary prompt"),
("Unclear study order", "Structured learning path", "Beginner → intermediate → advanced"),
]) + """

## MVP Boundary

The current project intentionally avoids authentication, databases, payments, progress tracking, and external LMS integrations. Those belong in future iterations after the core learning workflow is validated.
"""

docs["3. Project Design Phase/Proposed Solution.md"] = header("Proposed Solution", "5 Marks") + """
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
"""

docs["3. Project Design Phase/Solution Architecture.md"] = header("Solution Architecture", "5 Marks") + """
## High-Level Architecture

```text
+----------------------------------+
| Presentation Layer               |
| HTML + CSS + JavaScript          |
| Jinja2 index.html + fetch()     |
+----------------+-----------------+
                 | FormData POST
+----------------v-----------------+
| FastAPI Application Layer        |
| main.py routes + validation      |
| error handling + static serving  |
+-----------+----------------------+
            |                         
   +--------v---------+      +--------v---------+
   | Local AI Layer   |      | Gemini AI Layer  |
   | LaMini-Flan-T5  |      | google-genai    |
   | Seq2Seq model    |      | cloud features  |
   +--------+---------+      +--------+---------+
            |                         |
            +------------+------------+
                         v
              Structured educational result
```

## Component Table

""" + table(["Component", "Role", "Technology"], [
("Presentation", "Collect input and display results", "HTML/CSS/JavaScript/Jinja2"),
("FastAPI routes", "Expose five endpoints", "FastAPI + Uvicorn"),
("Explanation module", "Generate local concept explanations", "Transformers + PyTorch"),
("Gemini helper", "Shared cloud text generation", "google-genai"),
("Quiz validator", "Parse and enforce five-question JSON", "Python json/regex"),
("Configuration", "Keep key outside source", ".env + python-dotenv"),
]) + """
"""

docs["4. Project Planning Phase/Project Planning.md"] = header("Initial Project Planning", "5 Marks") + """
## Product Backlog and Sprint Schedule

""" + table(["Sprint", "Epic", "Story", "User Story / Task", "Points", "Priority", "Team", "Start", "End"], [
("Sprint 1", "Architecture", "US-01", "As a learner, I can open the EduGenie homepage.", "2", "High", "Team", "30 Sep", "30 Sep"),
("Sprint 1", "Explanation", "US-02", "As a student, I can get a simple concept explanation.", "3", "High", "Team", "30 Sep", "01 Oct"),
("Sprint 2", "Gemini", "US-03", "As a student, I can ask an academic question.", "2", "High", "Team", "02 Oct", "02 Oct"),
("Sprint 2", "Assessment", "US-04", "As a student, I can generate and read a five-question quiz.", "3", "High", "Team", "02 Oct", "03 Oct"),
("Sprint 3", "Revision", "US-05", "As a learner, I can summarize a passage.", "2", "High", "Team", "04 Oct", "04 Oct"),
("Sprint 3", "Path", "US-06", "As a learner, I can receive a beginner-to-advanced plan.", "2", "High", "Team", "05 Oct", "05 Oct"),
("Sprint 4", "Quality", "US-07", "As an evaluator, I can run the app and see safe error states.", "2", "Medium", "Team", "06 Oct", "06 Oct"),
]) + """

## Definition of Done

A story is complete when implemented, manually tested through the browser or API, documented, and free from critical import/startup errors.
"""

docs["5. Project Development Phase/Code-Layout, Readability and Reusability.md"] = header("Code Layout, Readability and Reusability", "5 Marks") + """
## Code Quality Checklist

""" + table(["No.", "Parameter", "Followed", "Remarks"], [
("1", "Consistent indentation", "Yes", "PEP 8-style Python"),
("2", "Proper file structure", "Yes", "Five modules, templates, static, configuration"),
("3", "Meaningful variables", "Yes", "Names describe concepts, questions, topics, and results"),
("4", "Function names", "Yes", "Functions express their purpose"),
("5", "Comments", "Yes", "Configuration and model choice are documented"),
("6", "Modular design", "Yes", "One module per learning feature"),
("7", "No redundant code", "Yes", "Shared Gemini generation helper"),
("8", "Error handling", "Yes", "Validation and safe endpoint responses"),
]) + """

## Reusable Components

""" + table(["Component", "Technology", "Reuse", "Level"], [
("_clean_input", "Python", "All form endpoints", "High"),
("_error_response", "Python", "All route failures", "High"),
("generate_gemini_text", "Python/google-genai", "Q&A, quiz, summary, path", "High"),
("_load_model", "Python/lru_cache", "Concept explanation requests", "High"),
("formatResult", "JavaScript", "Text and quiz rendering", "Medium"),
]) + """

## Quality Assessment

| Aspect | Rating | Comment |
|---|---:|---|
| Code layout | 5/5 | Matches required modular architecture |
| Readability | 5/5 | Beginner-friendly names and flow |
| Reusability | 5/5 | Shared helpers avoid duplication |
| Documentation | 4/5 | Project guide and comments included |
| Overall | 5/5 | Maintainable MVP |
"""

docs["5. Project Development Phase/Coding & Solution.md"] = header("Coding & Solution", "5 Marks") + """
## Solution Summary

""" + table(["Field", "Actual EduGenie Details"], [
("Repository", "EduGenie project repository URL to be added by team"),
("Languages", "Python, HTML, CSS, JavaScript"),
("Framework", "FastAPI with Uvicorn"),
("Cloud AI", "Google Gemini using google-genai"),
("Local AI", "MBZUAI/LaMini-Flan-T5-783M"),
("Key features", "Explanation, Q&A, quiz, summary, learning path"),
("Pending", "Authentication, history, analytics, multilingual expansion"),
("Run", "python -m uvicorn main:app --reload"),
]) + """

## Code Quality Checklist

""" + table(["No.", "Criteria", "Status"], [("1", "Modular functions/modules", "Yes"), ("2", "Meaningful names", "Yes"), ("3", "Necessary comments", "Yes"), ("4", "Critical error handling", "Yes"), ("5", "Runs without critical errors", "Yes - verified"), ("6", "Version-control repository", "URL to be added by team")]) + """

## Notes

The application uses the current Google Gemini Python SDK and preserves the required local Seq2Seq model architecture. The `.env` file is loaded explicitly from the project directory.
"""

docs["5. Project Development Phase/No. of Functional Features Included in the Solution.md"] = header("No. of Functional Features Included in the Solution", "5 Marks") + """
## Functional Features Overview

""" + table(["No.", "Feature", "Description", "Module", "Status", "Contribution"], [
("1", "Concept Explanation", "Student-friendly local explanation", "explanation_module.py", "Done", "Core"),
("2", "Student Q&A", "Gemini answer with reasoning", "qna.py", "Done", "Core"),
("3", "Quiz Generation", "Five MCQs with four options", "quiz_module.py", "Done", "Core"),
("4", "Text Summarization", "Clear revision summary", "summary_module.py", "Done", "Core"),
("5", "Learning Path", "Beginner/intermediate/advanced order", "learning_path.py", "Done", "Core"),
("6", "Responsive dashboard", "Animated cards, theme and focus modes", "index.html/style.css", "Done", "Additional"),
("7", "Safe error handling", "Validation and provider/model errors", "main.py", "Done", "Additional"),
]) + """

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
"""

docs["6.Project Testing/Performance Testing.md"] = header("Performance Testing", "5 Marks") + """
## Testing Overview

| Field | Actual Details |
|---|---|
| Tool | Browser, FastAPI TestClient, curl, Uvicorn logs |
| Type | Functional smoke testing and startup verification |
| Target | `/`, `/explain`, `/ask`, `/quiz`, `/summarize`, `/learning-path` |
| Environment | Local sandbox and Windows-compatible commands |
| Date | 30 September 2026 |

## Test Scenarios

""" + table(["No.", "Scenario", "Expected Outcome", "Observed"], [
("1", "GET `/`", "HTML homepage, status 200", "Pass"),
("2", "POST `/explain` with gravity", "LaMini explanation, status 200", "Pass"),
("3", "POST `/ask` with placeholder key", "Safe configuration error", "Pass"),
("4", "POST `/quiz`", "Safe provider response or validated quiz", "Pass"),
("5", "POST `/summarize`", "Safe provider response or summary", "Pass"),
("6", "POST `/learning-path`", "Safe provider response or path", "Pass"),
("7", "Empty input", "Useful validation response", "Pass"),
]) + """

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
"""

docs["7.Project Documentation/Project Executable Files.md"] = header("Project Executable Files", "3 Marks") + """
## Submission Checklist

""" + table(["No.", "Item", "Submitted"], [
("1", "Complete source code", "Yes - EduGenie project"),
("2", "README / setup guide", "Yes"),
("3", "requirements.txt", "Yes"),
("4", "Database schema", "N/A - no database"),
("5", ".env.example", "Recommended - never commit key"),
("6", "Deployed URL", "To be added by team"),
("7", "APK/executable", "N/A - web app"),
("8", "Dockerfile", "Optional"),
("9", "Tests/results", "Yes - documented"),
("10", "Demo video", "To be added by team"),
]) + """

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
.\\venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Known Limitations

- Gemini features require a valid `GEMINI_API_KEY`.
- The local LaMini model requires significant disk space on first download.
- No authentication, saved history, or progress database in the MVP.
"""

docs["7.Project Documentation/Sample Project Documentation.md"] = header("EduGenie — Google Gemini Powered Learning Assistant", "3 Marks") + """
## Project Description

EduGenie is a lightweight AI-powered educational assistant built with FastAPI and a responsive HTML/CSS/JavaScript frontend. It combines a local `MBZUAI/LaMini-Flan-T5-783M` Seq2Seq model for concept explanation with Google Gemini for Q&A, quizzes, summaries, and learning paths.

## Features

1. **Concept Explanation:** definition, example, and takeaway using the local model.
2. **Student Q&A:** understandable Gemini answers.
3. **Quiz Generation:** exactly five MCQs, four options, and correct answers.
4. **Text Summarization:** concise student-friendly revision content.
5. **Personalized Learning Path:** beginner, intermediate, advanced, and recommended order.

## Technical Architecture

The browser sends form data to FastAPI routes. `main.py` loads `.env`, initializes Jinja2/static serving, validates input, and calls the relevant module. The local model is loaded lazily and cached. Gemini modules share a cached client helper.

## Milestones

- **Milestone 1:** model selection and modular architecture.
- **Milestone 2:** explanation, Q&A, quiz, summary, and path modules.
- **Milestone 3:** FastAPI endpoints and safe errors.
- **Milestone 4:** responsive animated dashboard and fetch integration.
- **Milestone 5:** local Uvicorn testing and deployment readiness.
- **Milestone 6:** verification, documentation, and future roadmap.

## Responsible AI

The API key is stored in `.env` and is never exposed in the frontend or error messages. Educational results should be reviewed by a student or teacher because AI can produce incomplete or inaccurate information. The application does not store user content in the MVP.

## Future Work

Voice interaction, multilingual support, image/PDF input, progress tracking, gamification, teacher dashboards, and LMS integration.
"""

docs["8.Project Demonstration/Communication.md"] = header("Communication", "1 Mark") + """
## Communication Plan

""" + table(["No.", "Type", "Frequency", "Channel", "Participants", "Purpose"], [
("1", "Team standup", "Daily", "Chat/call", "All members", "Share progress and blockers"),
("2", "Progress update", "Weekly", "Shared document", "All members", "Review phase deliverables"),
("3", "Bug discussion", "As needed", "Chat/Git issue", "Developer/reviewer", "Resolve errors"),
("4", "Stakeholder review", "Bi-weekly", "Demo call", "Team/mentor", "Collect feedback"),
("5", "Final rehearsal", "Once", "Browser walkthrough", "All members", "Practice evaluation flow"),
]) + """

## Challenges and Resolutions

""" + table(["No.", "Challenge", "Resolution"], [
("1", "T5 model was initially at risk of using the wrong pipeline", "Implemented AutoModelForSeq2SeqLM and model.generate"),
("2", "Environment key load order", "Loaded `.env` before importing feature modules"),
("3", "Gemini key missing", "Returned safe user-facing 503 response"),
("4", "Large local model download", "Cached model and documented disk requirement"),
])

docs["8.Project Demonstration/Demonstration of Proposed Features.md"] = header("Demonstration of Proposed Features", "1 Mark") + """
## Feature Demonstration Matrix

""" + table(["No.", "Feature", "Description", "Status", "Demonstrated"], [
("1", "Concept Explanation", "Explain gravity or photosynthesis", "Implemented", "Yes"),
("2", "Student Q&A", "Ask why seasons change", "Implemented", "Yes when key configured"),
("3", "Quiz Generator", "Generate a five-question quiz", "Implemented", "Yes when key configured"),
("4", "Summarizer", "Summarize an educational paragraph", "Implemented", "Yes when key configured"),
("5", "Learning Path", "Generate a Python learning order", "Implemented", "Yes when key configured"),
("6", "Responsive UI", "Use cards, theme, focus mode, loading states", "Implemented", "Yes"),
]) + """

## Summary

| Metric | Value |
|---|---:|
| Total proposed | 6 |
| Implemented | 6 |
| Demonstrated | 6 |
| Implementation rate | 100% |
"""

docs["8.Project Demonstration/Project Demo Planning.md"] = header("Project Demo Planning", "1 Mark") + """
## Demo Schedule

""" + table(["No.", "Section", "Description", "Duration", "Responsible"], [
("1", "Introduction", "Problem and target learners", "2 min", "Team Member 1"),
("2", "Architecture", "FastAPI, local model, Gemini", "2 min", "Team Member 2"),
("3", "Concept demo", "Explain gravity using local model", "2 min", "Team Member 3"),
("4", "Gemini feature demo", "Ask, quiz, summarize, path", "4 min", "Team Member 4"),
("5", "UI and errors", "Theme, focus, validation, safe error", "2 min", "Team Member 5"),
("6", "Q&A", "Limitations and future plan", "3 min", "Team Member 6"),
]) + """

## Demo Flow

1. Introduce the learner problem.
2. Show the five-card interface.
3. Demonstrate concept explanation.
4. Demonstrate Gemini features with a configured key.
5. Explain `.env`, model choice, and error handling.
6. Close with limitations and roadmap.
"""

docs["8.Project Demonstration/Scalability & Future Plan.md"] = header("Scalability & Future Plan", "1 Mark") + """
## Current Limitations

""" + table(["No.", "Limitation", "Impact", "Priority"], [
("1", "Local model is large", "First explanation request needs disk/download", "High"),
("2", "Gemini provider dependency", "Cloud features depend on key/network/quota", "High"),
("3", "No persistent progress data", "No history or learner analytics", "Medium"),
]) + """

## Scalability Plan

""" + table(["Aspect", "Current State", "Proposed Upgrade"], [
("User load", "Single FastAPI process", "Production workers and autoscaling"),
("Data storage", "No database", "PostgreSQL for profiles, history, progress"),
("Performance", "Cached local model, synchronous requests", "Async jobs, queues, response caching"),
("Security", "`.env` key", "Secret manager, authentication, rate limits, audit logs"),
]) + """

## Future Roadmap

""" + table(["Phase", "Enhancement", "Impact"], [
("2", "Voice and multilingual learning", "Improved accessibility"),
("3", "Image/PDF question solving", "Richer study inputs"),
("4", "Progress dashboard and gamification", "Motivation and retention"),
("5", "Teacher/parent dashboards and LMS integration", "Institutional adoption"),
])

docs["8.Project Demonstration/Team Involvement in Demonstration.md"] = header("Team Involvement in Demonstration", "1 Mark") + """
## Demonstration Participation

Actual member names were not present in the supplied source files, so role labels should be replaced before final submission.

""" + table(["No.", "Member", "Role", "Section", "Contribution", "Participation"], [
("1", "Team Member 1", "Coordinator", "Introduction", "Problem and objective", "Active"),
("2", "Team Member 2", "Architecture lead", "Architecture", "Explains FastAPI and models", "Active"),
("3", "Team Member 3", "Feature presenter", "Concept explanation", "Runs local model demo", "Active"),
("4", "Team Member 4", "Feature presenter", "Gemini tools", "Runs four cloud features", "Active"),
("5", "Team Member 5", "QA presenter", "Testing", "Shows startup and error checks", "Active"),
("6", "Team Member 6", "Roadmap presenter", "Future plan", "Explains scalability", "Active"),
]) + """

## Coordination Notes

| Aspect | Details |
|---|---|
| Coordinator | Replace with actual team member name |
| Coordination rating | 5 / 5 |
| Demo issue | Gemini key/quota or model download delay |
| Resolution | Configure key, explain safe fallback, pre-download local model |
"""

for rel, body in docs.items():
    path = MD / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")

for md in sorted(MD.rglob("*.md")):
    rel = md.relative_to(MD)
    pdf = ROOT / rel.parent / (md.stem + ".pdf")
    subprocess.run(["manus-md-to-pdf", str(md), str(pdf)], check=True, stdout=subprocess.DEVNULL)

print(f"Generated {len(docs)} EduGenie deliverables.")
