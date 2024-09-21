import pandas as pd
import streamlit as st

# Load the rankings from the Excel file
data_file = 'pos_rankings.xlsx'

# Read the data for nouns, verbs, and adjectives from separate sheets
df_nouns = pd.read_excel(data_file, sheet_name='Nouns')
df_verbs = pd.read_excel(data_file, sheet_name='Verbs')
df_adjectives = pd.read_excel(data_file, sheet_name='Adjectives')

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging")
st.subheader("Top Nouns")
st.dataframe(df_nouns)

st.subheader("Top Verbs")
st.dataframe(df_verbs)

st.subheader("Top Adjectives")
st.dataframe(df_adjectives)

# Optional: Add interactivity
selected_noun = st.selectbox("Select a Noun", df_nouns['Nouns'])
st.write(f"You selected: {selected_noun}")

selected_verb = st.selectbox("Select a Verb", df_verbs['Verbs'])
st.write(f"You selected: {selected_verb}")

selected_adjective = st.selectbox("Select an Adjective", df_adjectives['Adjectives'])
st.write(f"You selected: {selected_adjective}")
