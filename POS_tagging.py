import spacy
import pandas as pd
import string
import re

# Load Spacy's English model for POS tagging
nlp = spacy.load("en_core_web_sm")

# Read captions from the specified Excel file and sheet
file_path = 'lg_standbyme_posts.xlsx'
captions_df = pd.read_excel(file_path, sheet_name='Sheet1')
captions = captions_df['Caption'].tolist()  # Assuming the column name is 'Caption'

# Create dictionaries to hold rankings and their counts
noun_count = {}
verb_count = {}
adj_count = {}

# Function to remove punctuation, emojis, Korean characters, and specific symbols
def clean_word(word):
    # Remove punctuation
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
    # Remove emojis and specific symbols using a regex pattern
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               "]+", flags=re.UNICODE)
    # Remove Korean characters and specific symbols
    cleaned_word = emoji_pattern.sub(r'', cleaned_word)
    cleaned_word = re.sub(r'[가-힣]', '', cleaned_word)  # Remove Korean characters
    return cleaned_word.strip()  # Remove extra spaces

# Perform POS tagging on each caption
for caption in captions:
    doc = nlp(caption)
    for token in doc:
        cleaned_word = clean_word(token.text.lower())
        if cleaned_word:  # Ensure the word is not empty after cleaning
            if token.pos_ == 'NOUN':
                noun_count[cleaned_word] = noun_count.get(cleaned_word, 0) + 1
            elif token.pos_ == 'VERB':
                verb_count[cleaned_word] = verb_count.get(cleaned_word, 0) + 1
            elif token.pos_ == 'ADJ':
                adj_count[cleaned_word] = adj_count.get(cleaned_word, 0) + 1

# Create dataframes for the nouns, verbs, and adjectives with counts
noun_df = pd.DataFrame(noun_count.items(), columns=['Nouns', 'Count']).sort_values(by='Count', ascending=False)
verb_df = pd.DataFrame(verb_count.items(), columns=['Verbs', 'Count']).sort_values(by='Count', ascending=False)
adj_df = pd.DataFrame(adj_count.items(), columns=['Adjectives', 'Count']).sort_values(by='Count', ascending=False)

# Write the dataframes to an Excel file with separate sheets
with pd.ExcelWriter('pos_rankings.xlsx') as writer:
    noun_df.to_excel(writer, sheet_name='Nouns', index=False)
    verb_df.to_excel(writer, sheet_name='Verbs', index=False)
    adj_df.to_excel(writer, sheet_name='Adjectives', index=False)

print("POS-based rankings saved to 'pos_rankings.xlsx'.")
