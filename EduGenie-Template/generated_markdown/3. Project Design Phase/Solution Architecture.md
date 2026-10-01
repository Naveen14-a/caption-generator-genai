# Solution Architecture

**Date:** 30 September 2026  
**Team ID:** SWTID-2026-3656  
**Project Name:** EduGenie – Google Gemini Powered Learning Assistant  
**Maximum Marks:** 5 Marks


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

| Component | Role | Technology |
|---|---|---|
| Presentation | Collect input and display results | HTML/CSS/JavaScript/Jinja2 |
| FastAPI routes | Expose five endpoints | FastAPI + Uvicorn |
| Explanation module | Generate local concept explanations | Transformers + PyTorch |
| Gemini helper | Shared cloud text generation | google-genai |
| Quiz validator | Parse and enforce five-question JSON | Python json/regex |
| Configuration | Keep key outside source | .env + python-dotenv |

