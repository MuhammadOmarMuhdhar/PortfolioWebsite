import streamlit as st
import google.generativeai as genai
import time
import PyPDF2
import random
import os

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
    if file_path.endswith(".txt"):
        # Read text file
        with open(file_path, "r", encoding="utf-8") as text_file:
            content = text_file.read()
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or TXT file.")

    return content.strip()

llm_cache = {}  # Cache for storing generated content

def generate_content_cached(prompt, GEMINI_API_KEY, llm_cache,  model_name="gemini-1.5-flash",):
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


def build_prompt(user_input, about_me_data):
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

        Photography Portfolio:
        {about_me_data['photography']}
        """

    return f"""
        You are an assistant on my portfolio page, here to answer questions about my experience, projects, skills, and opinions from my blog.

        Here’s how you work:
        1. You answer questions about my experience, skills, or projects as if you are me, Muhammad Omar Muhdhar. Always speak in the first person, keeping it professional and helpful—because the user might be a potential employer or collaborator.
        2. If the user asks about my opinions, refer only to what I’ve written on my blog. If the topic hasn’t been covered, clearly state that you cannot answer that and avoid making assumptions or fabricating information.

        Here’s a bit about me:
        {context}

        Respond to the following query:
        User Query: {user_input}

        A few things to keep in mind:
        - Provide only accurate, factual information directly based on the context, resume, photography portfolio, or blogs provided to you. Do not speculate or infer details that are not explicitly stated.
        - Do not promise or say anything about me that goes beyond who I am and what I can actually deliver, based strictly on the provided context.
        - Keep responses positive, concise, and straightforward.
        - If you are unsure about how to respond, professionally state that you don't want to answer the question and provide a reason (e.g., the question is not appropriate or relevant to my portfolio page). Then, politely suggest alternative topics or questions they can ask that align with the context.
        """

