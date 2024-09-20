import streamlit as st
import pandas as pd

# Load the data
data_file = 'lg_standbyme_posts.xlsx'
df = pd.read_excel(data_file)

# App title
st.title("Instagram Post Analysis")

# Display the DataFrame
st.subheader("Posts Data")
st.dataframe(df)

# Add more visualizations and features here
