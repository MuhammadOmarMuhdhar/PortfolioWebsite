import streamlit as st
import json  


projects = [

    {
        "Title": "Interactive Dashboard for Exploring Poverty Research",
        "Key-words": "API Integration, ETL Pipeline, Google BigQuery, Machine Learning, Scikit-learn, Gemini LLM, Academic Paper Classification, Streamlit Dashboard, Research Intelligence, Project Management",
        "Description": (
            "Integrated multiple third-party APIs (OpenAlex, CrossRef, PubMed) to build a centralized poverty studies "
            "database in Google BigQuery, developing a Python-based ETL pipeline to extract and process metadata for "
            "500,000+ academic papers spanning two decades. Developed a Python classification system using scikit-learn and "
            "Gemini LLM to automatically categorize and filter research papers. Designed a Streamlit dashboard interface that displays "
            "the categorized research data via interactive visualizations, enabling stakeholders to extract research "
            "intelligence for evidence-driven research prioritization. Managed the complete project lifecycle; defining "
            "requirements with stakeholders, overseeing architecture, implementing quality control measures, and "
            "conducting user training for platform adoption."
        ),
        "Link": "https://cega-literature-dashboard.streamlit.app", 
        "visuals": [
        {
        "path": "configurations/data/visuals/Poverty-Research-Map.jpg",
        "caption": "Poverty Research Map"
        }
        ],
    },

    {
    "Title": "Housing Affordability & Commuting Burdens: Displacement Challenges in Santa Clara County",
    "Key-words": "Housing Policy, Urban Planning, Statistical Analysis, R, OLS Regression, Chi-Square Testing, ACS Data, Transportation Equity, Displacement Analysis, GIS Mapping",
    "Description": "Examined the relationship between housing affordability and commuting patterns in Santa Clara County using American Community Survey 5-year estimates. Conducted comprehensive statistical analysis including OLS regression, chi-square tests, and logistic regression to investigate how rent burden (50%+ of income) affects commute times and transportation mode choices across census tracts. Analyzed racial disparities in commuting patterns while controlling for income and housing affordability factors. Created spatial visualizations mapping housing affordability categories and displacement risk indicators across the county. Found that moderate rent burdens significantly impact commuting behavior, and that workers in high-cost areas exhibit distinct transportation patterns including lower drive-alone rates and increased public transit usage among lower-income residents.",
    "Status": "Completed",
    "Link": "",
    "visuals": [
        {
        "path": "configurations/data/visuals/Poverty-Research-Map.jpg",
        "caption": "Housing Affordability Distribution Across Santa Clara County"
        }
    ]
    },
    {
        "Title": "Stability Forecasting: Data Science Applications in South Asian Peace Process Analysis",
        "Key-words": "Machine Learning, Random Forest, Peace Agreement Analysis, Conflict Prediction, International Relations, Data Science, Geopolitical Analysis, South Asia",
        "Description": (
            "Applied machine learning to analyze peace agreement durability using 2000+ agreements from the University of Edinburgh dataset. "
            "Developed a Random Forest model with 94.6% accuracy predicting agreement failures, identifying territorial disputes and "
            "para-statal forces as key breakdown predictors. Applied findings to the May 2025 India-Pakistan ceasefire following Kashmir "
            "attacks, revealing concerning sustainability prospects. Research shifts focus from predicting conflict onset to forecasting peace "
            "stability, proposing a live peace index for early warning indicators in this strategically important relationship."
        ),
        "Link": "https://placeholder-peace-forecasting-link.com",
        "visuals": [
            {
            "path": "configurations/data/visuals/Political Risk Analysis.jpg",
            "caption": "Peace Agreement Classification by Territorial and Comprehensiveness Factors"
            }
        ]
    },
    
    
]

with open("configurations/data/projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)