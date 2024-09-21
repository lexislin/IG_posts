import nltk
from collections import Counter
import pandas as pd
import streamlit as st

# Download necessary NLTK data (only needs to run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load your Instagram post data
data_file = 'lg_standbyme_posts.xlsx'
df = pd.read_excel(data_file)

# Extract captions
captions = df['Caption'].dropna().tolist()

# Tokenize and POS tag the captions
tokens = []
for caption in captions:
    words = nltk.word_tokenize(caption)
    tagged = nltk.pos_tag(words)
    tokens.extend(tagged)

# Separate tokens into nouns, verbs, and adjectives
nouns = [word for word, pos in tokens if pos.startswith('NN')]
verbs = [word for word, pos in tokens if pos.startswith('VB')]
adjectives = [word for word, pos in tokens if pos.startswith('JJ')]

# Count frequencies of nouns, verbs, and adjectives
noun_counts = Counter(nouns)
verb_counts = Counter(verbs)
adjective_counts = Counter(adjectives)

# Convert to DataFrame for easier handling and display
df_nouns = pd.DataFrame(noun_counts.items(), columns=['Noun', 'Count']).sort_values(by='Count', ascending=False)
df_verbs = pd.DataFrame(verb_counts.items(), columns=['Verb', 'Count']).sort_values(by='Count', ascending=False)
df_adjectives = pd.DataFrame(adjective_counts.items(), columns=['Adjective', 'Count']).sort_values(by='Count', ascending=False)

# Streamlit Display
st.title("Instagram Post Analysis with POS Tagging")
st.subheader("Top Nouns")
st.dataframe(df_nouns.head(10))
st.subheader("Top Verbs")
st.dataframe(df_verbs.head(10))
st.subheader("Top Adjectives")
st.dataframe(df_adjectives.head(10))
