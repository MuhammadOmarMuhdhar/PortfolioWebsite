import streamlit as st
import google.generativeai as genai
from config import creds
import time

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
    Builds the prompt for the Gemini LLM to provide meaningful responses.
    """
    return f"""
    You are an intelligent assistant designed to provide detailed and thoughtful answers about my experience, projects, and skills. 
    Respond professionally and helpfully to the following user query:
    
    User: {user_input}
    """

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Welcome to my Bot! Feel free to ask questions about my experience, projects, or skills.\n\n"
            "Here are some example questions you can ask:\n"
            "- Can you tell me about your recent projects?\n"
            "- What areas of expertise do you have?\n"
            "- Have you worked on machine learning or data analysis projects?\n"
            "- What technologies are you proficient in?\n"
            "- What is your experience in computational social science?\n"
            "- Can you share details about your portfolio or achievements?"
        )
    })

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
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
        for i in range(typing_time):
            placeholder.markdown(f"Thinking{'.',* (i % 3 + 1)}")
            time.sleep(1)

        # Display the response
        placeholder.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
