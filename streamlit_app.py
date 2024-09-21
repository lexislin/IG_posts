import streamlit as st
import pandas as pd

# Load the data
data_file = 'lg_standbyme_posts.xlsx'
df = pd.read_excel(data_file)

# App title
st.title("Instagram Post Analysis")

# Display the DataFrame
st.subheader("Posts Data")
st.dataframe(df)

# Display basic statistics
st.subheader("Basic Statistics")
st.write("Total Posts:", df.shape[0])
st.write("Average Likes:", df['Likes'].mean())
st.write("Average Comments:", df['Comments'].mean())

# Add visualizations
st.subheader("Likes and Comments Distribution")
st.bar_chart(df[['Likes', 'Comments']])

# Additional visualizations
# Example: Word cloud for captions
if st.button("Generate Word Cloud for Captions"):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    text = " ".join(caption for caption in df['Caption'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud for Captions")
    st.pyplot(plt)

# Further analysis options can be added here
