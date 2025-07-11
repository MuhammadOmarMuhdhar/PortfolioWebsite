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
        "Status": "Completed",
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
        "path": "configurations/data/visuals/commute percentage by race.jpg",
        "caption": "Housing Affordability Distribution Across Santa Clara County"
        }
    ]
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