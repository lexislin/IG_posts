import pandas as pd
import streamlit as st
import altair as alt

# Load the rankings from the Excel file
data_file = 'pos_rankings.xlsx'
df_nouns = pd.read_excel(data_file, sheet_name='Nouns')
df_verbs = pd.read_excel(data_file, sheet_name='Verbs')
df_adjectives = pd.read_excel(data_file, sheet_name='Adjectives')

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging")

# Toggle selection for charts
option = st.selectbox("Select the type of chart to display:", ['Top Nouns', 'Top Verbs', 'Top Adjectives'])

# Create charts using Altair for better aesthetics
if option == 'Top Nouns':
    st.subheader("Top Nouns")
    chart = alt.Chart(df_nouns.head(10)).mark_bar(color='skyblue').encode(
        y=alt.Y('Nouns:N', sort='-x'),
        x='Count:Q',
        tooltip=['Nouns', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)
    
elif option == 'Top Verbs':
    st.subheader("Top Verbs")
    chart = alt.Chart(df_verbs.head(10)).mark_bar(color='salmon').encode(
        y=alt.Y('Verbs:N', sort='-x'),
        x='Count:Q',
        tooltip=['Verbs', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)
    
elif option == 'Top Adjectives':
    st.subheader("Top Adjectives")
    chart = alt.Chart(df_adjectives.head(10)).mark_bar(color='lightgreen').encode(
        y=alt.Y('Adjectives:N', sort='-x'),
        x='Count:Q',
        tooltip=['Adjectives', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

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
