import docx2txt
from PyPDF2 import PdfReader
import tempfile

def parse_resume(uploaded_file):
    """
    Extracts text from uploaded resume (PDF or DOCX).
    """

    text = ""

    try:
        if uploaded_file.name.endswith(".pdf"):
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            reader = PdfReader(tmp_path)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + " "

        elif uploaded_file.name.endswith(".docx"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            text = docx2txt.process(tmp_path)

        else:
            text = "Unsupported file type."

    except Exception as e:
        text = f"Error reading file: {str(e)}"

    return text.strip()
