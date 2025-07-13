import streamlit as st
from configurations import functions
# from config import creds
import json
import random
import time
import os
from configurations import project_files, blog_files
import base64
from streamlit_tree_select import tree_select
import pandas as pd
import plotly.graph_objects as go
import sys
sys.path.append('configurations/data/visuals')
from sankey import Sankey


st.set_page_config(
    page_title="Muhammad Omar Muhdhar",
    layout= "centered")

st.markdown("""
        <style>   
        #MainMenu {visibility: hidden;}       
        </style>
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


GEMINI_API_KEY = os.environ.get("API_KEY")

llm_cache = {}

def _update_session_state(processed_selections):
    """Updates session state with new selections"""
    for key, value in processed_selections.items():
        st.session_state.ui_state[key] = value

def load_filters_json():
    """Load filters JSON"""
    with open('configurations/data/labels.json', 'r') as f:
        return json.load(f)
    
def build_tree_optimized(data, path=""):
    """Optimized tree builder"""
    if not data:
        return []
    
    tree = []
    for key, value in data.items():
        node_path = f"{path} > {key}" if path else key
        
        if isinstance(value, dict):
            children = build_tree_optimized(value, node_path)
            tree.append({
                "label": key,
                "value": node_path,
                "children": children
            })
        elif isinstance(value, list):
            children = [
                {"label": item, "value": f"{node_path} > {item}"} 
                for item in value
            ]
            tree.append({
                "label": key,
                "value": node_path,
                "children": children
            })
    return tree

def load_and_process_filters():
    """Cache the filter loading and tree building"""
    filters = load_filters_json()
    
    study_types_tree = build_tree_optimized(filters['study_types'])
    mechanisms_tree = build_tree_optimized(filters['mechanisms']) 
    behaviors_tree = build_tree_optimized(filters['Behaviors'])
    
    return filters, study_types_tree, mechanisms_tree, behaviors_tree

def process_tree_selections(selections, min_depth=2):
    """Process tree selections"""
    if not selections or not selections.get('checked'):
        return []
    
    result = []
    for value in selections['checked']:
        parts = value.split(' > ')
        if len(parts) >= min_depth:
            result.append(parts[min_depth - 1])
    return result

def _process_current_selections(filters):
    """Processes current UI selections into usable format"""
    selected_contexts = st.session_state.get("sankey_contexts", [])
    selected_study_types = st.session_state.get("sankey_study_types", {})
    selected_mechanisms = st.session_state.get("sankey_mechanisms", {})
    selected_behaviors = st.session_state.get("sankey_behaviors", {})
    
    all_selected_context = []
    for context_key in selected_contexts:
        # Handle the case where poverty_contexts values are strings, not lists
        context_value = filters['poverty_contexts'][context_key]
        if isinstance(context_value, list):
            all_selected_context.extend(context_value)
        else:
            all_selected_context.append(context_value)
    
    all_selected_study_types = process_tree_selections(selected_study_types, min_depth=3)
    all_selected_mechanisms = process_tree_selections(selected_mechanisms, min_depth=2)
    all_selected_behaviors = process_tree_selections(selected_behaviors, min_depth=2)
    
    return {
        'contexts': all_selected_context,
        'study_types': all_selected_study_types,
        'mechanisms': all_selected_mechanisms,
        'behaviors': all_selected_behaviors
    }

def render_filters():
    """Renders the filter UI and processes selections"""
    filters, study_types_tree, mechanisms_tree, behaviors_tree = load_and_process_filters()
    
    _render_filter_ui(filters, study_types_tree, mechanisms_tree, behaviors_tree)
    
    processed_selections = _process_current_selections(filters)
    _update_session_state(processed_selections)



def _render_filter_ui(filters, study_types_tree, mechanisms_tree, behaviors_tree):
    """Renders all filter UI components"""
    st.markdown("**Poverty Contexts**")
    st.multiselect(
        "Select contexts",
        list(filters['poverty_contexts'].keys()),
        key="sankey_contexts",
        label_visibility="collapsed"
    )
    
    st.markdown("**Study Types**")
    tree_select(study_types_tree, key="sankey_study_types")
    
    st.markdown("**Mechanisms**")
    tree_select(mechanisms_tree, key="sankey_mechanisms")
    
    st.markdown("**Behaviors**")
    tree_select(behaviors_tree, key="sankey_behaviors")

@st.cache_data
def load_sankey_data():
    """Load and cache the poverty research data"""
    return pd.read_csv('configurations/data/poverty_data_for_visualization.csv')

def explode_comma_separated_data(df, columns_to_explode):
    """
    Explode comma-separated values in specified columns into separate rows
    """
    df_exploded = df.copy()
    
    # Split comma-separated values and strip whitespace
    for col in columns_to_explode:
        if col in df_exploded.columns:
            # Split on comma and strip whitespace
            df_exploded[col] = df_exploded[col].astype(str).str.split(',').apply(
                lambda x: [item.strip() for item in x] if isinstance(x, list) else [str(x).strip()]
            )
    
    # Explode each column sequentially
    for col in columns_to_explode:
        if col in df_exploded.columns:
            df_exploded = df_exploded.explode(col)
    
    # Clean up any empty or invalid entries
    for col in columns_to_explode:
        if col in df_exploded.columns:
            df_exploded = df_exploded[
                (df_exploded[col] != '') & 
                (df_exploded[col] != 'nan') & 
                (df_exploded[col].notna()) &
                (df_exploded[col] != 'Insufficient info')
            ]
    
    return df_exploded.reset_index(drop=True)

def render_interactive_sankey():
    """Renders the interactive filter + Sankey diagram for Masters Capstone project"""
    
    # Initialize session state for UI if needed
    if 'ui_state' not in st.session_state:
        st.session_state.ui_state = {}
    
    # Load and preprocess data
    df_raw = load_sankey_data()
    
    # Explode comma-separated values in key columns
    columns_to_explode = ['study_type', 'poverty_context', 'mechanism', 'behavior']
    df = explode_comma_separated_data(df_raw, columns_to_explode)
    
    filters_json = load_filters_json()
    
    # Get current filter selections (using original render_filters function)
    processed_selections = _process_current_selections(load_filters_json())
    
    # Create Sankey instance
    sankey = Sankey(filters_json=filters_json)
    
    # Define columns to show in the diagram
    columns_to_show = ['poverty_context', 'study_type', 'mechanism', 'behavior']
    
    # Create and display the Sankey diagram (full width)
    try:
        # Start with broad categories (detail level 1) unless filters are applied
        manual_detail_level = 1 if not any(processed_selections.values()) else None
        
        fig = sankey.draw(
            df=df, 
            columns_to_show=columns_to_show,
            active_filters=processed_selections,
            manual_detail_level=manual_detail_level
        )
        
        # Make the visualization more compact and add spacing for titles
        fig.update_layout(
            height=350, 
            width=900,
            margin=dict(t=80, b=20, l=20, r=20)  # Add top margin for title spacing
        )
        
        # Adjust annotation positioning to be further from the diagram
        if fig.layout.annotations:
            updated_annotations = []
            for annotation in fig.layout.annotations:
                if hasattr(annotation, 'y') and annotation.y == 1.1:  # This is likely a column header
                    # Create new annotation with updated y position
                    new_annotation = go.layout.Annotation(
                        x=annotation.x,
                        y=1.15,  # Move title further up
                        text=annotation.text,
                        showarrow=annotation.showarrow,
                        xref=annotation.xref,
                        yref=annotation.yref,
                        font=annotation.font
                    )
                    updated_annotations.append(new_annotation)
                else:
                    updated_annotations.append(annotation)
            fig.update_layout(annotations=updated_annotations)
        
        st.plotly_chart(fig, use_container_width=True, height=350)
        
        # Add description
        st.caption("Interactive visualization showing relationships between poverty contexts, study methods, psychological mechanisms, and behavioral outcomes in academic literature. This sample is part of a larger dashboard - view the full interactive dashboard via the link in 'See more' below.")
        
    except Exception as e:
        st.error(f"Error generating visualization: {str(e)}")
        st.info("Please adjust your filter selections or try again.")
    
    # Expandable horizontal filters at the bottom
    with st.expander("🎛️ Filters (Click to expand)", expanded=False):
        # Create horizontal layout for filters
        filters, study_types_tree, mechanisms_tree, behaviors_tree = load_and_process_filters()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("**Poverty Contexts**")
            st.multiselect(
                "Select contexts",
                list(filters['poverty_contexts'].keys()),
                key="sankey_contexts",
                label_visibility="collapsed"
            )
        
        with col2:
            st.markdown("**Study Types**")
            tree_select(study_types_tree, key="sankey_study_types")
        
        with col3:
            st.markdown("**Mechanisms**")
            tree_select(mechanisms_tree, key="sankey_mechanisms")
        
        with col4:
            st.markdown("**Behaviors**")
            tree_select(behaviors_tree, key="sankey_behaviors")

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
        
        for i, project in enumerate(projects):
            with st.container():
                st.markdown(f"### {project['Title']}")
                # Keywords
                st.write(f"**Keywords:** {project['Key-words']}")
                
                # Special handling for Masters Capstone project - show interactive visual
                if "Poverty Research" in project['Title'] or "CEGA" in project['Title']:
                    # Show interactive Sankey diagram instead of static image
                    render_interactive_sankey()
                else:
                    # Regular visual showcase for other projects
                    if project.get('visuals'):
                        # Create columns for multiple images
                        if len(project['visuals']) > 1:
                            cols = st.columns(len(project['visuals']))
                            for j, visual in enumerate(project['visuals']):
                                with cols[j]:
                                    st.image(visual['path'], caption=visual['caption'], use_column_width=True)
                        else:
                            st.image(project['visuals'][0]['path'], caption=project['visuals'][0]['caption'])
               
                # Expandable full details
                with st.expander("See more"):
                    st.markdown(f"**Description:** {project['Description']}")
                    
                    
                    # Links
                    col1, col2 = st.columns(2)
                    with col1:
                        if project['Link']:
                            st.markdown(f"[View Project]({project['Link']})")
                  
                
                st.markdown("---")

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