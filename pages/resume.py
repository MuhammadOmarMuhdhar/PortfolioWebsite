import streamlit as st
import base64

st.markdown(
        """
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 175px;
           max-width: 175px;
       }
       """,
        unsafe_allow_html=True,
    )  

# Title for the app
st.title("My Resume")

# Embed the PDF in an iframe for viewing
pdf_path = "pages/Resume_Muhammad Muhdhar-DataScientist2.pdf" 
with open(pdf_path, "rb") as f:
    pdf_data = f.read()

# Encode PDF data to base64
pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

# Display the PDF
st.markdown(f"""
<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500" type="application/pdf"></iframe>
""", unsafe_allow_html=True)

# Provide a download button for the resume
st.download_button(
    label="Download My Resume",
    data=pdf_data,
    file_name="My_Resume.pdf",
    mime="application/pdf",
)