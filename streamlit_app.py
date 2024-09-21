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
    plt.figure(figsize=(10, 6))
    plt.barh(df_nouns['Nouns'][:10], df_nouns['Count'][:10], color='skyblue')
    plt.xlabel('Count')
    plt.ylabel('Nouns')
    plt.title('Top Nouns')
    st.pyplot(plt)
    
elif option == 'Top Verbs':
    st.subheader("Top Verbs")
    plt.figure(figsize=(10, 6))
    plt.barh(df_verbs['Verbs'][:10], df_verbs['Count'][:10], color='salmon')
    plt.xlabel('Count')
    plt.ylabel('Verbs')
    plt.title('Top Verbs')
    st.pyplot(plt)
    
elif option == 'Top Adjectives':
    st.subheader("Top Adjectives")
    plt.figure(figsize=(10, 6))
    plt.barh(df_adjectives['Adjectives'][:10], df_adjectives['Count'][:10], color='lightgreen')
    plt.xlabel('Count')
    plt.ylabel('Adjectives')
    plt.title('Top Adjectives')
    st.pyplot(plt)

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
