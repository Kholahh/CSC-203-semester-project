AI_Resume_Screener


A minimal, **offline-friendly** Python Streamlit app that accepts **PDF resumes** and a **Job Description** (paste or .txt file), then analyzes and ranks how well the CV matches the job.


This version is intentionally simple — it uses TF-IDF (scikit-learn) for similarity and does **not** require large external models or system binaries.


## Files
- `app.py` — main Streamlit app (UI + workflow)
- `resume_parser.py` — extract text from PDF (and optional DOCX)
- `text_processing.py` — text cleaning and simple skill extraction
- `similarity_model.py` — TF-IDF similarity and scoring
- `requirements.txt` — packages to install
- `sample_job_description.txt` — example job description


## Quick setup (Windows / Mac / Linux)
1. Open VS Code and open an integrated terminal.
2. Create project folder and move files there (or save files directly in that folder).


```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Mac / Linux:
source venv/bin/activate


pip install -r requirements.txt