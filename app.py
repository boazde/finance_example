import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import altair as alt

# Define the Streamlit app
def app():
    st.title("CSV File Viewer")
    st.write("This app reads a CSV file and presents the data in a table.")
    
    # Load the CSV file
    file = "data.csv"
    
    # Show the data
    df = pd.read_csv(file)
    st.write(df)
    
    # Show some basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())
    

    
# Run the app
if __name__ == "__main__":
    app()
