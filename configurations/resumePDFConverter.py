import PyPDF2

resume_file_path = "/Users/muhammadmuhdhar/Desktop/Repo/PortfolioWebsite/Resume_Muhammad_Muhdhar.pdf" 

content = ""
with open(resume_file_path, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        content += page.extract_text()
        
# Save to a text file
with open("resume.txt", "w") as f:
    f.write(content)