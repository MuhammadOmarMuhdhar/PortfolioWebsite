import streamlit as st 
from configurations import project_files

st.markdown(
    """
    <style>
    [data-testid="stExpanderToggleIcon"] {
        display: none;
        pointer-events: none; /* Disables any interaction */
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

projects = project_files.projects

for project in projects:
    with st.expander("", expanded=True):
        st.markdown(f"#### {project['Title']}")
        st.write(f"**Key Words:** {project['Key-words']}")
        st.markdown(f"**Description:** {project['Description']}")
        # st.write(f"**Technologies Used:** {project['Technologies']}")
        st.write(f'**Status:** {project["Status"]}')
        st.markdown(f"[View Project]({project['Link']})")
