import streamlit as st

col1, col2 = st.columns([1, 1])

# Add an image in the first column
col1.write(" ")
col1.write(" ")

col1.image(
        'portrait.jpg', 
        # caption='Muhammad Muhdhar Portrait', 
        use_container_width=True, 
        output_format='PNG', 
        width=200
    )

# Add "About Me" content in the second column
col2.write("### About Me")
col2.markdown("""
    Hello, I’m **Muhammad Muhdhar**, a Master’s student in Computational Social Science at UC Berkeley. My current work centers on leveraging unsupervised machine learning and large language models (LLMs) to process and analyze unstructured human data, such as open-ended survey responses, and transform it into actionable insights. Applications include product feedback, course evaluations, and employee engagement surveys, with additional potential for studying trends and topics on social media.

    Before UC Berkeley, I earned my undergraduate degree in **Government and Philosophy** at UT Austin. After graduation, I worked as a consultant at Ernst & Young. Outside of my academic and professional pursuits, I am photographer. I also enjoy writing about my interests in technology and its broader societal impact. 
                  
    """)
