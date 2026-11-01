import streamlit as st
import pandas as pd
from sparql_processor import run_sparql_query


st.title("Film Finder")
film_name   = st.text_input("Enter a film name:")

if st.button("Search"):
    if film_name:
        results = run_sparql_query(sparql_param=film_name, sparql_file="./sparql_queries/film_title.sparql")
        if results and "results" in results and "bindings" in results["results"]:
            titles = [result["title"]["value"] for result in results["results"]["bindings"]]
            df = pd.DataFrame(titles, columns=["Film Titles"])
            st.dataframe(df)
        else:
            st.write("No results found.")
    else:
        st.write("Please enter a film name to search.")     