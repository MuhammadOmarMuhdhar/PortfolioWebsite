import streamlit as st
import json  


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
    },
    {
    "Title": "Density-Aware Spatial Data Rescaling",
    "Key-words": "Data Engineering, GIS, GeoPandas, ETL (Extract, Transform, Load)",
    "Description": (
        "This project develops a methodology for rescaling demographic and spatial data between different geographic boundaries "
        "while accounting for intra-unit population density variations. Unlike traditional areal interpolation methods that assume "
        "uniform distribution within source units, this approach incorporates auxiliary data (e.g., nighttime lights, building density, "
        "traffic patterns) to estimate sub-unit population density variations. The methodology is particularly valuable when transforming "
        "data between disparate boundary systems (e.g., census tracts to watersheds) where population distribution is highly heterogeneous. "
        "The project demonstrates significant improvements in accuracy compared to conventional area-weighted approaches, especially in "
        "regions with diverse land use patterns and varying population densities."
        ),
        "Status": "On-going",
        "Link": "https://github.com/MuhammadOmarMuhdhar/geoscaler" 
    }
]

with open("configurations/data/projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)