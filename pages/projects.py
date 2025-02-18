import streamlit as st 

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
projects = [
    {
        "Title": "Economic Lessons From the FIFA World Cup on Brazil",
        "Key-words": "Economics, Data Analysis, Python, Difference-in-Differences (DiD), Synthetic Control Method (SCM)",
        "Description": (
            "This project analyzed the economic and environmental impacts of hosting the 2014 FIFA "
            "World Cup in Brazil. Key tasks included automating data retrieval using APIs, conducting "
            "Difference-in-Differences (DiD) and Synthetic Control Method (SCM) analyses to assess "
            "causal effects on host states versus non-host states, and creating a policy memo with "
            "recommendations for sustainable mega-event planning."
        ),
        "Status": "Completed",
        "Link": "https://github.com/MuhammadOmarMuhdhar/WorldCupHostCities_Impact"
    },
    {
        "Title": "Statistical Significance in Topic Modeling",
        "Key-words": "NLP, Topic Modeling, Causal Analysis, BERTopic, Transformers, Python",
         "Description": (
        "This project explores the potential application of topic modeling within social science research. "
        "Using IMDB reviews of the Netflix series *Squid Game* as a case study, the project "
        "demonstrates how Natural Language Processing (NLP) techniques can be tailored for causal explanatory purposes. "
        "The key contribution of this project is a methodology for statistically validating topic models by measuring their ability to explain behavioral outcomes - "
        "in this case, how BERTopic discovered discussion themes in reviews explain user ratings of the show Squid Game. "
        ),
        "Status": "On-going",
        "Link": "https://github.com/MuhammadOmarMuhdhar/Statistical-Significance-in-Topic-Modeling"
    }
]


for project in projects:
    with st.expander("", expanded=True):
        st.markdown(f"#### {project['Title']}")
        st.write(f"**Key Words:** {project['Key-words']}")
        st.markdown(f"**Description:** {project['Description']}")
        # st.write(f"**Technologies Used:** {project['Technologies']}")
        st.write(f'**Status:** {project["Status"]}')
        st.markdown(f"[View Project]({project['Link']})")
