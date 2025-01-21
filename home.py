import streamlit as st
from configurations import functions
from config import creds
import json
import random
import time
import os

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
GEMINI_API_KEY = creds.GEMINI_API_KEY

llm_cache = {}

def main():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Ensure session state is initialized
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""

    phtographyfile_path = 'configurations/photography.txt'
    if 'photography' not in st.session_state:
            st.session_state.photography = functions.load_resume(phtographyfile_path)
            phtography_content = st.session_state.photography
    else:
            phtography_content = st.session_state.photography

    if 'about_me' not in st.session_state:
        resume_file_path = "configurations/resume.txt"  
        resume_content = functions.load_resume(resume_file_path)
       
        
        with open("configurations/data/blogs.json", "r", encoding="utf-8") as f:
            blogs = json.load(f)
        about_me_data = {
            'about_me': """
                        Hello, I’m Muhammad Muhdhar, a Master’s student in Computational Social Science at UC Berkeley. My current interests centers on leveraging Transformer-based and Probabilistic topic modeling in tandem with LLMs to process and analyze unstructured human data. 
                                                
                        Before UC Berkeley, I earned my undergraduate degree in Government and Philosophy at UT Austin and worked as a consultant at Ernst & Young. Outside my academic and professional work, I am a hobbyist photographer.
            """,
            'blogs': blogs, 
            'resume': resume_content,
            'photography': st.session_state.photography
        }
        st.session_state.about_me = about_me_data
    else:
        about_me_data = st.session_state.about_me


    # st.write(st.session_state.about_me)

    # Main content
    with st.container():
    # Main layout with two columns
        col1, col2 = st.columns([11, 1])

        with st.expander("", expanded=True):
                # Introductory content and buttons at the top
            with st.container():
                        # Nested layout for image and "About Me" content
                img_col, text_col = st.columns([1, 2.5])  # Adjust proportions for better balance

                        # Add an image in the first column
                with img_col:
                            st.image(
                                'portrait.jpg',
                                width=250,  # Adjust the width to make the image smaller
                                output_format='PNG'
                            )
                            st.markdown(" ")

                with text_col:
                            st.markdown("##### About Me")
                            st.markdown(about_me_data['about_me'])


        
        # Chatbot section
        st.markdown('------')
        st.markdown("""
                Curious to know more about me? Feel free to ask the chatbot below about my background, projects, skills, or personal interests. 
        """)

        st.markdown("###### Examples of what you can ask:")
        col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 10])

        with st.container():

                with col3:
                    if st.button("\U0001F4DE", help="Contact"):
                        st.session_state.prompt = "How can I reach you?"
                with col4:
                    if st.button("\U0001F5C2", help="Experience"):
                        # List of random questions
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
                        # List of random questions
                        random_questions = [
                            "What are you studying at UC Berkeley?",
                            "Can you share insights about your current projects?",
                            "What courses have you taken?",
                            "How does your academic work relate to industry?"
                        ]
                        st.session_state.prompt = random.choice(random_questions)

                with col6:
                    if st.button("\U0001F680", help="Personal Interests"):
                        # List of random questions
                        random_questions = [
                            "What is your opinion on the future of AI?",
                            "What is one way you think technology has impacted society?",
                            "Tell me about your photography Style.",
                            "What is your favorite photography subject?",
                        ]
                        st.session_state.prompt = random.choice(random_questions)

        # Display chat messages (kept below the intro and buttons)
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input or button
    prompt = st.chat_input("Ask a question") or st.session_state.get("prompt", "")
    if prompt:
            # Clear the temporary prompt state if used
            st.session_state.pop("prompt", None)

            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Typing animation for bot response
            with st.chat_message("assistant"):
                placeholder = st.empty()

                # Build the context-aware prompt
                full_prompt = functions.build_prompt(prompt, about_me_data)

                # Generate response using Gemini LLM and get actual time taken
                try:
                    response, actual_time = functions.generate_content_cached(prompt=full_prompt, GEMINI_API_KEY=GEMINI_API_KEY, llm_cache=llm_cache)
                except Exception as e:
                    response = f"Sorry, I encountered an error: {e}"
                    actual_time = 3  # Default fallback time

                # Simulate typing with actual time taken
                typing_time = max(1, int(actual_time))  # Ensure at least 1 second
                for i in range(typing_time * 3):  # Typing cycles with all three dots
                    dots = '.' * ((i % 3) + 1)
                    placeholder.markdown(f"Thinking{dots}")
                    time.sleep(0.5)

                # Display the response
                placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()