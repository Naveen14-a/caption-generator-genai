# Define Problem Statements

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 3 Marks


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
