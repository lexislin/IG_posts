import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load the data
data_file = 'lg_standbyme_posts.xlsx'
df = pd.read_excel(data_file)

# App title
st.title("Instagram Post Analysis")

# Display the DataFrame
st.subheader("Posts Data")
st.dataframe(df)

# Function to clean the text (remove hashtags and certain terms)
def clean_text(text, stopwords):
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove special characters and extra spaces
    text = re.sub(r'[\n\r]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove specific stopwords (e.g., product names, brand terms)
    for stopword in stopwords:
        text = text.replace(stopword, '')
    
    return text

# Define words to remove (stopwords)
stopwords = ['StanbyME Go', 'LG', 'LGTV', 'personalscreen', 'lifestylescreen', 'Take a moment', 'Turntable', 'wallpaper']

# Combine all captions into a single string after cleaning them
all_captions = ' '.join(df['Caption'].apply(lambda x: clean_text(x, stopwords)))

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_captions)

# Display the word cloud
st.subheader("Word Cloud")
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Split the cleaned text into words
words = all_captions.split()

# Count word frequencies
word_counts = Counter(words)

# Convert to a DataFrame for easier display
word_freq_df = pd.DataFrame(word_counts.items(), columns=['Keyword', 'Frequency']).sort_values(by='Frequency', ascending=False)

# Display the top keywords and their frequencies
st.subheader("Top Keywords")
st.dataframe(word_freq_df.head(20))  # Display top 20 keywords
