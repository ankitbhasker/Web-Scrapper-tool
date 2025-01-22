# app.py
import streamlit as st
from scraper import scrape_and_analyze

st.title("AI Web Scraper and Analyzer")

# Input field for the URL
url = st.text_input("Enter the URL to scrape:")

# Button to trigger scraping and analysis
if st.button("Scrape and Analyze"):
    with st.spinner("Scraping the website..."):
        try:
            result = scrape_and_analyze(url)
            st.success("Scraping and analysis complete!")
            st.write("**Analysis Result:**")
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {e}")