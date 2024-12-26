
# import streamlit as st

# # Title for the app
# st.title("My Resume")

# # Embed the PDF in an iframe for viewing
# pdf_path = "/Users/muhammadmuhdhar/Desktop/Repo/PortfolioWebsite/Resume_Muhammad Muhdhar-Master.pdf"  # Replace with your PDF file path
# with open(pdf_path, "rb") as f:
#     pdf_data = f.read()

# # Display the PDF
# st.markdown(f"""
# <iframe src="data:application/pdf;base64,{pdf_data.encode('base64').decode()}" width="700" height="500" type="application/pdf"></iframe>
# """, unsafe_allow_html=True)

# # Provide a download button for the resume
# st.download_button(
#     label="Download My Resume",
#     data=pdf_data,
#     file_name="My_Resume.pdf",
#     mime="application/pdf",
# )
