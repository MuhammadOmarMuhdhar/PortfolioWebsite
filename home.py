import streamlit as st
import google.generativeai as genai
from config import creds
import time
from pages import blog
import PyPDF2
import random

# Page Configuration
st.set_page_config(
    page_title="Muhammad Muhdhar Portfolio",
    page_icon="📘",
    # layout="wide",  # Use wide layout
    initial_sidebar_state="expanded"  # Collapse the left menu
)

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

def load_resume(file_path):
    """
    Reads resume content from a file (PDF or TXT).
    """
    if file_path.endswith(".pdf"):
        # Extract text from PDF
        content = ""
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                content += page.extract_text()
    elif file_path.endswith(".txt"):
        # Read text file
        with open(file_path, "r", encoding="utf-8") as text_file:
            content = text_file.read()
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or TXT file.")

    return content.strip()

# Load resume
resume_file_path = "/Users/muhammadmuhdhar/Desktop/Repo/PortfolioWebsite/Resume_Muhammad Muhdhar-Master.pdf"  
resume_content = load_resume(resume_file_path)

# Update your about_me_data dictionary
about_me_data = {
    'about_me': """
Hello, I’m **Muhammad Muhdhar**, a Master’s student in Computational Social Science at UC Berkeley. My current work centers on leveraging unsupervised machine learning and large language models (LLMs) to process and analyze unstructured human data, such as open-ended survey responses, and transform it into actionable insights. Applications include product feedback, course evaluations, and employee engagement surveys, with additional potential for studying trends and topics on social media.

Before UC Berkeley, I earned my undergraduate degree in **Government and Philosophy** at UT Austin. After graduation, I worked as a consultant at Ernst & Young. Outside of my academic and professional pursuits, I am a photographer. I also enjoy writing about my interests in technology and its broader societal impact.
""",
    'blogs': blog.blogs,  # Assuming blogs is already defined
    'resume': resume_content  # Dynamically loaded resume content
}

# Configure Gemini API Key
GEMINI_API_KEY = creds.GEMINI_API_KEY

# Cache for LLM responses
llm_cache = {}

def generate_content_cached(prompt, model_name="gemini-1.5-flash"):
    """
    Generates content using a generative model with caching to avoid redundant calls.
    """
    # Configure Gemini
    genai.configure(api_key=GEMINI_API_KEY)

    # Check if the prompt is already cached
    if prompt in llm_cache:
        output = llm_cache[prompt]  # Retrieve from cache
    else:
        start_time = time.time()  # Record start time

        # Use the generative model
        gemini_model = genai.GenerativeModel(model_name)
        output = gemini_model.generate_content(prompt).text  # Generate content

        # Cache the output
        llm_cache[prompt] = output

        # Record the actual time taken
        end_time = time.time()
        llm_cache[f"{prompt}_time"] = end_time - start_time

    return output, llm_cache.get(f"{prompt}_time", 3)  # Default time if not recorded

def build_prompt(user_input):
    """
    Builds the prompt for the Gemini LLM to provide meaningful responses, incorporating about_me_data.
    """
    context = f"""
About Me:
{about_me_data['about_me']}

Blogs:
{about_me_data['blogs']}

Resume:
{about_me_data['resume']}
"""

    return f"""
Hi there! I’m your assistant here to answer questions about my experience, projects, skills, and even my opinions from my blog. 

Here’s a bit about me: 
{context}

Here’s how I work:
1. I’ll answer questions about my experience, skills, or projects as if I’m Muhammad Omar Muhdhar. I’ll always speak in the first person, keeping it professional and helpful—because you’re probably a potential employer or collaborator, right?
2. If you ask about my opinions, I’ll refer to what I’ve written on my blog. If I haven’t covered the topic, I’ll let you know rather than making something up.

A few things to keep in mind:
- I’ll only provide accurate, factual info based on what’s in my context or blog. 
- I won’t exaggerate, embellish, or promise anything I can’t deliver. 
- I’ll keep it positive and straightforward, no unnecessary fluff or negativity.

So, go ahead! Ask me something:
User Query: {user_input}
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Ensure session state is initialized
if "prompt" not in st.session_state:
    st.session_state.prompt = ""
with st.container():
    # Main layout with two columns
    col1, col2 = st.columns([11, 1])

    # Left column (col1) content
    # with col1: 
    with st.expander("", expanded=True):
            # Introductory content and buttons at the top
        with st.container():
                    # Nested layout for image and "About Me" content
            img_col, text_col = st.columns([1, 2.5])  # Adjust proportions for better balance

                    # Add an image in the first column
            with img_col:
                        # st.markdown(" ")
                        # st.markdown(" ")
                        # st.markdown(" ")
                        st.image(
                            'portrait.jpg',
                            width=250,  # Adjust the width to make the image smaller
                            output_format='PNG'
                        )
                        st.markdown(" ")

                    # Add "About Me" content in the second column
            with text_col:
                        st.markdown("##### About Me")
                        st.markdown("""
                            Hello, I’m Muhammad Muhdhar, a Master’s student in Computational Social Science at UC Berkeley. My current interests centers on leveraging Transformer-based and Probabilistic topic modeling in tandem with LLMs to process and analyze unstructured human data. 
                                    
                            Before UC Berkeley, I earned my undergraduate degree in Government and Philosophy at UT Austin and worked as a consultant at Ernst & Young. Outside my academic and professional work, I enjoy photography and writing about technology's impact on society.
                        """)



    # # Right column (col2) content
    # with col2: 

       
    #         # Add buttons with spacing adjustments

    #         if st.button('💻 ', key="blog_button", help="Explore my blog posts"):
    #             st.write("You clicked Blog!")

    #         if st.button('📄 ', key="resume_button", help="View my resume"):
    #             st.write("You clicked Resume!")

    #         if st.button('📷 ', key="photo_button", help="Check out my photography portfolio"):
    #             st.write("You clicked Photography!")

    #         st.markdown("")
    #         st.markdown("")
    #         st.markdown("")
    #         st.markdown("")
                                    

                
                        




    # Introduce the chatbot functionality
st.markdown('------')
st.markdown("""
        Curious to know more about me? Feel free to ask the chatbot below about my background, projects, skills, or personal interests. 
        """)
        
        # Add example questions with buttons
st.markdown("###### Examples of what you can ask:")
col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 10])

with st.container():

        with col3:
            if st.button("\U0001F4DE"):
                st.session_state.prompt = "How can I reach you?"
        with col4:
            if st.button("\U0001F5C2"):
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
            if st.button("\U0001F4DA"):
                # List of random questions
                random_questions = [
                    "What are you studying at UC Berkeley?",
                    "Can you share insights about your current projects?",
                    "What courses have you taken?",
                    "How does your academic work relate to industry?"
                ]
                st.session_state.prompt = random.choice(random_questions)

        with col6:
            if st.button("\U0001F680"):
                # List of random questions
                random_questions = [
                    "What ethical challenges do you see in AI?",
                    "How do you think machine learning can impact society positively?",
                    "What risks do you identify of biased algorithms?",
                    "Do you think AI will replace human creativity?"
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
        full_prompt = build_prompt(prompt)

        # Generate response using Gemini LLM and get actual time taken
        try:
            response, actual_time = generate_content_cached(full_prompt)
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
