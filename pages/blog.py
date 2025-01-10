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

st.markdown(
    """
    <style>
    :root {
        --primary-color: #1d70b8;
        --background-color: #121212;
        --secondary-background-color: #1e1e1e;
        --text-color: #e0e0e0;
        --font-family: 'sans-serif';
    }
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stSidebar {
        background-color: var(--secondary-background-color);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
        """
       <style>
            [data-testid="stSidebar"][aria-expanded="true"]{
                min-width: 175px;
                max-width: 175px;
            }
       <style>
       """,
        unsafe_allow_html=True,
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

blogs = blog_files.blogs   

# Debug: Log query parameters
query_params = st.query_params
# st.write("Query Parameters:", query_params)  # Debug print

# Retrieve the 'blog' query parameter
selected_blog_id = query_params.get("blog", [None])
# st.write("Selected Blog ID:", selected_blog_id)  # Debug print

if query_params == {} or selected_blog_id == "":
    # st.title("Blog")  # Page title

    for blog in blogs:
        # Display the title of each blog
        st.subheader(blog["title"])

        # Create columns for layout (title and summary/date)
        col1, col2 = st.columns([4, 1])

        # Show blog summary in the first column, if available
        if 'summary' in blog:
            col1.write(blog["summary"])

        # Show blog date in the second column, if available
        if 'date' in blog:
            col2.write(f"*{blog['date']}*")

        # Add a "Read More" link to view the full blog with the corresponding query parameter
        st.markdown(f"[Read More](?blog={blog['id']})")

        # Add a horizontal divider between blogs
        st.markdown("---")
elif selected_blog_id:
    # If a specific blog is selected, find it by its ID
    selected_blog = next((blog for blog in blogs if blog["id"] == selected_blog_id), None)
    
    if selected_blog:
        # Display the full details of the selected blog
        st.title(selected_blog["title"])  # Blog title
        st.write(f"*{selected_blog['date']}*")  # Blog date
        st.markdown(selected_blog["content"])  # Blog content
        st.markdown("[Back to All Blogs](?blog=)")  # Link to return to the main blog list
    else:
        # Handle invalid blog ID
        st.error("Blog not found. Please check the URL.")
