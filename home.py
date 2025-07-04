import streamlit as st
from configurations import functions
# from config import creds
import json
import random
import time
import os
from configurations import project_files, blog_files
import base64

st.set_page_config(
    page_title="Muhammad Omar Muhdhar",
    layout= "centered")

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
    [data-testid="stExpanderToggleIcon"] {
        display: none;
        pointer-events: none; /* Disables any interaction */
    }
    </style>
    """,
    unsafe_allow_html=True
)

GEMINI_API_KEY = os.environ.get("API_KEY")

llm_cache = {}

def main():

    # Title with LinkedIn icon
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <h1 style="margin: 0; margin-right: 15px;">Muhammad Omar Muhdhar</h1>
            <a href="https://www.linkedin.com/in/muhammad-omar-muhdhar/" target="_blank" style="text-decoration: none;">
                <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="25" style="vertical-align: middle;">
            </a>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Home", "Projects", "Blog", "Resume"])

    with tab1:
        st.markdown(" ")
        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "prompt" not in st.session_state:
            st.session_state.prompt = ""

        # Load about_me data
        if 'about_me' not in st.session_state:
            resume_file_path = "configurations/resume.txt"  
            resume_content = functions.load_resume(resume_file_path)
        
            with open("configurations/data/blogs.json", "r", encoding="utf-8") as f:
                blogs = json.load(f)

            with open("configurations/data/projects.json", "r", encoding="utf-8") as f:
                projects = json.load(f)

            about_me_data = {
                'about_me': """
                            Hello, I'm Muhammad Muhdhar, a recent graduate from Berkeley's Computational Social Science program. I am a data scientist with experience in building scalable data infrastructure, developing machine learning solutions, and creating analytics platforms that bridge technical implementation with business strategy.
                            
                            I earned my undergraduate degree in Government and Philosophy at UT Austin and worked as a Business Analyst at Ernst & Young. Outside my academic and professional work, I am a hobbyist photographer.
   """,
                'blogs': blogs, 
                'projects': projects,
                'resume': resume_content
            }
            st.session_state.about_me = about_me_data
        else:
            about_me_data = st.session_state.about_me

        # Profile section - using expander
        # with st.expander("", expanded=True):
        img_col, text_col = st.columns([1, 2.5])
        
        with img_col:
            st.image(
                'portrait.jpg',
                width=250,
                output_format='PNG'
            )
            st.markdown(" ")

        with text_col:
            st.markdown("### About Me")
            st.markdown(about_me_data['about_me'])

        # Chatbot introduction

        col1, col2 = st.columns([6, 10])
        with col1:
            st.markdown('------')
        st.markdown("""
                Curious to know more about me? Feel free to ask the chatbot below about my background, projects, skills, or personal interests. 
        """)

        # Example buttons
        st.markdown("###### Examples of what you can ask:")
        col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 10])

        with col3:
            if st.button("\U0001F4DE", help="Contact"):
                st.session_state.prompt = "How can I reach you?"
        
        with col4:
            if st.button("\U0001F5C2", help="Experience"):
                random_questions = [
                    "Do you have data science experience?",
                    "Tell me about your experience at EY.",
                    "What did you learn as a consultant at EY?",
                    "What projects have you worked on?",
                    "What industries have you worked in?",
                    "What technologies do you specialize in?"
                ]
                st.session_state.prompt = random.choice(random_questions)
        
        with col5:
            if st.button("\U0001F4DA", help="Education"):
                random_questions = [
                    "What is your educational background?",
                    "Can you share insights about your current projects?",
                    "What courses have you taken?",
                    "How does your academic work relate to industry?"
                ]
                st.session_state.prompt = random.choice(random_questions)

        with col6:
            if st.button("\U0001F680", help="Personal Interests"):
                random_questions = [
                    "What is your opinion on the future of AI?",
                    "What is one way you think technology has impacted society?",
                    "What's your preferred tech stack for data pipeline development?"
                ]
                st.session_state.prompt = random.choice(random_questions)

        # Display all existing chat messages
        for i, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                # Show thinking animation for the latest assistant message if it's being processed
                if (message["role"] == "assistant" and 
                    i == len(st.session_state.messages) - 1 and 
                    st.session_state.get("processing_response", False)):
                    
                    placeholder = st.empty()
                    
                    # Build the context-aware prompt for the previous user message
                    user_msg = st.session_state.messages[i-1]["content"]
                    full_prompt = functions.build_prompt(user_msg, about_me_data)

                    # Generate response using Gemini LLM
                    try:
                        response, actual_time = functions.generate_content_cached(
                            prompt=full_prompt, 
                            GEMINI_API_KEY=GEMINI_API_KEY, 
                            llm_cache=llm_cache
                        )
                    except Exception as e:
                        response = f"Sorry, I encountered an error: {e}"
                        actual_time = 3

                    # Simulate typing with actual time taken
                    typing_time = max(1, int(actual_time))
                    for j in range(typing_time * 3):
                        dots = '.' * ((j % 3) + 1)
                        placeholder.markdown(f"Thinking{dots}")
                        time.sleep(0.5)

                    # Update the message content and mark as processed
                    st.session_state.messages[i]["content"] = response
                    st.session_state.processing_response = False
                    
                    # Display the final response
                    placeholder.markdown(response)

                    # Add disclaimer
                    st.markdown(
                        """
                        <div style="text-align: left; padding: 10px 0;">
                            <p style="color: var(--st-color-gray-900); font-size: 0.8em; margin: 0; opacity: .5;">
                                AI can hallucinate. Please verify any information.
                            </p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                else:
                    # Display regular message
                    st.markdown(message["content"])

        # Add spacing before chat input
        st.write("")
        st.write("")
        
        # Chat input - MUST be the very last element in tab1 for bottom positioning
        prompt = st.chat_input("Ask a question") or st.session_state.get("prompt", "")
        
        # Process user input and add placeholder for response
        if prompt:
            # Clear the temporary prompt state if used from buttons
            st.session_state.pop("prompt", None)

            # Add user message and placeholder assistant message to session state
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": "..."})  # Placeholder
            st.session_state.processing_response = True
            
            # Rerun to display the new messages in the correct position with thinking animation
            st.rerun()

    with tab2:
        projects = project_files.projects

        for project in projects:
            with st.expander("", expanded=True):
                st.markdown(f"#### {project['Title']}")
                st.write(f"**Key Words:** {project['Key-words']}")
                st.markdown(f"**Description:** {project['Description']}")
                st.write(f'**Status:** {project["Status"]}')
                st.markdown(f"[View Project]({project['Link']})")

    with tab3:
        blogs = blog_files.blogs
        
        for i, blog in enumerate(blogs):
            with st.container():
                st.markdown(f"### {blog['title']}")
                
                # Meta information
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.caption(f"📅 {blog['date']}")
                with col2:
                    st.caption(f"📖 {len(blog['content'].split())} words")
                with col3:
                    st.caption(f"⏱️ {max(1, len(blog['content'].split()) // 200)} min read")
                
                # Show preview
                preview = blog['content'][:200] + "..." if len(blog['content']) > 200 else blog['content']
                st.markdown(preview)
                
                # Expandable full content
                with st.expander("Read full post"):
                    st.markdown(blog["content"])
                
                st.markdown("---")

    with tab4:
        # Embed the PDF in an iframe for viewing
        pdf_path = "configurations/Resume - Muhammad Muhdhar.pdf" 
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()

        # Encode PDF data to base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

        # Display the PDF
        st.markdown(f"""
        <iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500" type="application/pdf"></iframe>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()