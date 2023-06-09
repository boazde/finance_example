import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import altair as alt

# Define the Streamlit app
def app():
    st.title("Finance Viewer")
    st.write("This app can also filter and show analytics of the data.")
    
    # Load the CSV file
    file = "data.csv"
    
    # Show the data
    df = pd.read_csv(file)
    st.write(df)
    
    # Show some basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())
    
    chart = alt.Chart(df).mark_bar().encode(
    x='W-1',
    y='count()'
    )
    st.altair_chart(chart, use_container_width=True)
    
# Run the app
if __name__ == "__main__":
    app()
