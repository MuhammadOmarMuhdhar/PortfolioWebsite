import streamlit as st
import json  


projects = [

    {
        "Title": "Masters Capstone – Center for Effective Global Action (CEGA)",
        "Key-words": "Data Engineering, NLP, LLMs, ETL, Streamlit, Visualization, OpenAlex, Gemini, Transformers",
        "Description": (
            "Built an automated ETL pipeline integrating OpenAlex and CrossRef APIs to extract research paper metadata into Google Sheets. "
            "Developed a transformer-based classification model to categorize academic papers by topic using annotated corpus, and leveraged "
            "Gemini LLMs to generate narrative summaries for strategic decision-making. Created an interactive Streamlit dashboard with "
            "contour graphs and density maps visualizing topic distributions and research trends. Collaborated cross-functionally through "
            "iterative user testing to ensure accessibility for non-technical stakeholders."
        ),
        "Status": "Completed",
        "Link": "https://cega-literature-dashboard.streamlit.app"
    },
    {
        "Title": "Housing Displacement Risk Analysis for Climate-Vulnerable Populations",
        "Key-words": "Policy Research, R, Statistical Analysis, Data Visualization, Database Development, Environmental Justice, Housing Policy",
        "Description": (
            "Analyzed housing displacement risk among climate-vulnerable populations, focusing on income disparities and housing cost burdens "
            "across demographic groups. Performed statistical analysis in R to evaluate housing burden and eviction risk patterns, creating "
            "demographic maps and temporal charts. Compiled multi-source datasets from American Community Survey and Eviction Lab at census "
            "tract level, designing database architecture for scalable risk assessment across 1.78 million residents. Delivered comprehensive "
            "reports with data-driven policy recommendations for environmental and social justice goals."
        ),
        "Status": "Completed",
        "Link": ""
    },
    {
        "Title": "Economic Lessons From the FIFA World Cup on Brazil",
        "Key-words": "Economics, Data Analysis, Python, Difference-in-Differences (DiD), Synthetic Control Method (SCM)",
        "Description": (
            "Analyzed economic and environmental impacts of hosting the 2014 FIFA World Cup in Brazil. "
            "Automated data retrieval using APIs and conducted Difference-in-Differences (DiD) and "
            "Synthetic Control Method (SCM) analyses to assess causal effects on host versus non-host states. "
            "Created policy memo with recommendations for sustainable mega-event planning."
        ),
        "Status": "Completed",
        "Link": "https://github.com/MuhammadOmarMuhdhar/WorldCupHostCities_Impact"
    },
    {
    "Title": "Density-Aware Spatial Data Rescaling",
    "Key-words": "Data Engineering, GIS, GeoPandas, ETL (Extract, Transform, Load)",
    "Description": (
        "Develops methodology for rescaling demographic and spatial data between geographic boundaries while accounting for "
        "intra-unit population density variations. Unlike traditional areal interpolation assuming uniform distribution, incorporates "
        "auxiliary data (nighttime lights, building density, traffic patterns) to estimate sub-unit density variations. Particularly "
        "valuable for transforming data between disparate boundary systems (census tracts to watersheds) with heterogeneous population "
        "distribution. Demonstrates significant accuracy improvements over conventional area-weighted approaches in diverse land use regions."
        ),
        "Status": "Completed",
        "Link": "https://github.com/MuhammadOmarMuhdhar/geoscaler" 
    },
    
]

with open("configurations/data/projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)