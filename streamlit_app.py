import nltk
import os
from collections import Counter
import pandas as pd
import streamlit as st

# Function to ensure NLTK data is downloaded
def download_nltk_data():
    nltk_data_dir = os.path.expanduser('~/nltk_data')
    if not os.path.exists(nltk_data_dir):
        os.makedirs(nltk_data_dir)

    # Check if 'punkt' is available, and download if not
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', download_dir=nltk_data_dir)
    
    # Check for 'averaged_perceptron_tagger' and download if missing
    try:
        nltk.data.find('taggers/averaged_perceptron_tagger')
    except LookupError:
        nltk.download('averaged_perceptron_tagger', download_dir=nltk_data_dir)

# Ensure the NLTK data is available
download_nltk_data()

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
st.data
