from textblob import TextBlob
import pandas as pd
import streamlit as st
from collections import Counter

# Load your Instagram post data
data_file = 'lg_standbyme_posts.xlsx'
df = pd.read_excel(data_file)

# Extract captions
captions = df['Caption'].dropna().tolist()

# Tokenize and POS tag the captions using TextBlob
nouns, verbs, adjectives = [], [], []

for caption in captions:
    blob = TextBlob(caption)
    for word, pos in blob.tags:
        if pos.startswith("NN"):  # Nouns
            nouns.append(word)
        elif pos.startswith("VB"):  # Verbs
            verbs.append(word)
        elif pos.startswith("JJ"):  # Adjectives
            adjectives.append(word)

# Count frequencies of nouns, verbs, and adjectives
noun_counts = Counter(nouns)
verb_counts = Counter(verbs)
adjective_counts = Counter(adjectives)

# Convert to DataFrame for easier handling and display
df_nouns = pd.DataFrame(noun_counts.items(), columns=['Noun', 'Count']).sort_values(by='Count', ascending=False)
df_verbs = pd.DataFrame(verb_counts.items(), columns=['Verb', 'Count']).sort_values(by='Count', ascending=False)
df_adjectives = pd.DataFrame(adjective_counts.items(), columns=['Adjective', 'Count']).sort_values(by='Count', ascending=False)

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging (TextBlob)")
st.subheader("Top Nouns")
st.dataframe(df_nouns.head(10))
st.subheader("Top Verbs")
st.dataframe(df_verbs.head(10))
st.subheader("Top Adjectives")
st.dataframe(df_adjectives.head(10))
