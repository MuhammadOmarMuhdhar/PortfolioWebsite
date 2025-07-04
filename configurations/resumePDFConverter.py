from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

resume_file_path = "configurations/Master-Resume-Muhammad Muhdhar.pdf"

content = ""
try:
    # Attempt to extract text with PyPDF2
    with open(resume_file_path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            content += page.extract_text()
except:
    pass

# If PyPDF2 fails or produces empty content, fall back to OCR
if not content.strip():
    images = convert_from_path(resume_file_path)  # Convert PDF pages to images
    for image in images:
        content += pytesseract.image_to_string(image)

# Save to a text file
with open("resume.txt", "w") as f:
    f.write(content)
