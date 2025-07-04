import streamlit as st
from configurations import blog_files
import json 

st.set_page_config(
    page_title="Muhammad Omar Muhdhar - Blog",
    layout= "centered",  # Use narrow layout
    initial_sidebar_state="expanded"  # Collapse the left menu
)

st.markdown( """

        <style>   
        #MainMenu {visibility: hidden;}       
        <style>

        """, unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Target the menu button */
    [data-testid="stSidebarCollapsedControl"] button svg {
        display: none; /* Hide the default icon */
    }
    
    [data-testid="stSidebarCollapsedControl"] button::before {
        content: '';
        display: inline-block;
        width: 30px;
        height: 25px;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="%23FFFFFF" d="M3 6h18v2H3V6zm0 5h18v2H3v-2zm0 5h18v2H3v-2z"></path></svg>');
        background-size: contain;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown(
#         """
#        <style>
#             [data-testid="stSidebar"][aria-expanded="true"]{
#                 min-width: 175px;
#                 max-width: 175px;
#             }
#        <style>
#        """,
#         unsafe_allow_html=True,
# ) 

st.sidebar.markdown("""
         <style>
            .sidebar-icons {
                    position: absolute;
                    bottom: -40px;
                    right: 80;
                    display: flex;
                    flex-direction: column;
                    align-items: flex-left;
                            }
            .sidebar-icons img {
                    width: 30px; /* Adjust size as needed */
                    margin-bottom: 10px;
                            }
        </style>
        <div class="sidebar-icons">
                    <a href="https://www.linkedin.com/in/muhammad-omar-muhdhar/" target="_blank">
                        <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="30">
                    </a>
        </div>
                        """,
                        unsafe_allow_html=True,
)

blogs = blog_files.blogs   

for blog in blogs:
    with st.expander(blog["title"] ):
        # st.write(blog["summary"])
        st.write(f"*{blog['date']}*")
        st.markdown(blog["content"])