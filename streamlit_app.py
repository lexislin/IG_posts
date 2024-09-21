import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the rankings from the Excel file
data_file = 'pos_rankings.xlsx'
df_nouns = pd.read_excel(data_file, sheet_name='Nouns')
df_verbs = pd.read_excel(data_file, sheet_name='Verbs')
df_adjectives = pd.read_excel(data_file, sheet_name='Adjectives')

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging")

# Toggle selection for charts
option = st.selectbox("Select the type of chart to display:", ['Top Nouns', 'Top Verbs', 'Top Adjectives'])

if option == 'Top Nouns':
    st.subheader("Top Nouns")
    st.bar_chart(df_nouns.set_index('Nouns')['Count'])
elif option == 'Top Verbs':
    st.subheader("Top Verbs")
    st.bar_chart(df_verbs.set_index('Verbs')['Count'])
elif option == 'Top Adjectives':
    st.subheader("Top Adjectives")
    st.bar_chart(df_adjectives.set_index('Adjectives')['Count'])

# Display the underlying data in a table
st.subheader("Data Table")
if option == 'Top Nouns':
    st.dataframe(df_nouns)
elif option == 'Top Verbs':
    st.dataframe(df_verbs)
elif option == 'Top Adjectives':
    st.dataframe(df_adjectives)

# Optional: Add a summary of the selected words
if option == 'Top Nouns':
    selected_word = st.selectbox("Select a Noun", df_nouns['Nouns'])
elif option == 'Top Verbs':
    selected_word = st.selectbox("Select a Verb", df_verbs['Verbs'])
else:
    selected_word = st.selectbox("Select an Adjective", df_adjectives['Adjectives'])

st.write(f"You selected: {selected_word}")
