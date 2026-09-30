# EduGenie — Google Gemini Powered Learning Assistant

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 3 Marks


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
