import PyPDF2
import docx2txt

def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_docx(file):
    doc = docx2txt.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def extract_resume_text(uploaded_file):
    if uploaded_file is None:
        return ""

    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        return extract_text_from_docx(uploaded_file)
    else:
        return ""