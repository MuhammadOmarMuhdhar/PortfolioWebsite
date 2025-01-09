import streamlit as st

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
st.title("Photography Portfolio")

# Path to the PDF file
pdf_path = "pages/Muhammad Muhdhar - Fine Art Photography Gallery.pdf"

# Create a link for users to open the PDF in another tab
st.markdown(
    f'<a href="file://{pdf_path}" target="_blank" style="font-size:18px;">Open My Photo Gallery in a New Tab</a>',
    unsafe_allow_html=True
)

# Provide a download button for the photo gallery
with open(pdf_path, "rb") as f:
    pdf_data = f.read()

st.download_button(
    label="Download My Photo Gallery",
    data=pdf_data,
    file_name="Muhammad_Muhdhar_Photo_gallery.pdf",
    mime="application/pdf",
)
