import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Load the rankings from the Excel file
data_file = 'pos_rankings.xlsx'
df_nouns = pd.read_excel(data_file, sheet_name='Nouns')
df_verbs = pd.read_excel(data_file, sheet_name='Verbs')
df_adjectives = pd.read_excel(data_file, sheet_name='Adjectives')

# Load all captions from the original data source
captions_file = 'lg_standbyme_posts.xlsx'
df_captions = pd.read_excel(captions_file, sheet_name='Sheet 1')
captions = df_captions['Caption'].dropna().tolist()

# Function to clean the text data
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'[\U0001F600-\U0001F64F]', '', text)  # Remove emojis
    return text.lower()

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging")

# Number input for customizing the number of records to show
num_records = st.number_input("Select the number of records to display:", min_value=1, max_value=50, value=10)

# Toggle selection for charts
option = st.selectbox("Select the type of chart to display:", ['Top Nouns', 'Top Verbs', 'Word Cloud'])

# Create charts using Altair for better aesthetics
if option == 'Top Nouns':
    st.subheader("Top Nouns")
    chart = alt.Chart(df_nouns.head(num_records)).mark_bar(color='skyblue').encode(
        y=alt.Y('Nouns:N', sort='-x'),
        x='Count:Q',
        tooltip=['Nouns', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)
    
elif option == 'Top Verbs':
    st.subheader("Top Verbs")
    chart = alt.Chart(df_verbs.head(num_records)).mark_bar(color='salmon').encode(
        y=alt.Y('Verbs:N', sort='-x'),
        x='Count:Q',
        tooltip=['Verbs', 'Count']
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

elif option == 'Word Cloud':
    st.subheader("Word Cloud")
    
    # Combine all captions
    combined_text = ' '.join(captions)
    
    # Clean the combined text
    cleaned_text = clean_text(combined_text)
    
    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Turn off axis
    st.pyplot(plt)

# Optional: Add a summary of the selected words
if option == 'Top Nouns':
    selected_word = st.selectbox("Select a Noun", df_nouns['Nouns'].head(num_records))
elif option == 'Top Verbs':
    selected_word = st.selectbox("Select a Verb", df_verbs['Verbs'].head(num_records))

st.write(f"You selected: {selected_word}")
