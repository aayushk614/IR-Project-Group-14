import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from sklearn.feature_extraction.text import CountVectorizer
from tweet_list import fetch_tweet


tweets = fetch_tweet()

# Preprocess the tweets
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(tweets)
X = X.toarray()

# Define cosine similarity function
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Calculate pairwise cosine similarity
n_tweets = len(tweets)
cosine_sim = np.zeros((n_tweets, n_tweets))
for i in range(n_tweets):
    for j in range(n_tweets):
        cosine_sim[i][j] = cosine_similarity(X[i], X[j])

# Define Streamlit app
def app():
    st.set_page_config(page_title="Tweet Similarity Analysis")

    # Display the tweet text
    st.subheader("Tweet Text")
    for i, tweet in enumerate(tweets):
        st.write(f"{i+1}. {tweet}")

    # Display the pairwise cosine similarity matrix
    st.subheader("Pairwise Cosine Similarity Matrix")
    df = pd.DataFrame(cosine_sim, columns=[f"Tweet {i+1}" for i in range(n_tweets)], index=[f"Tweet {i+1}" for i in range(n_tweets)])
    st.write(df)

    # Create a bar chart to visualize the pairwise cosine similarity matrix
    chart_data = pd.melt(df.reset_index(), id_vars=['index'], value_vars=df.columns)
    chart = alt.Chart(chart_data).mark_bar().encode(
        x='index',
        y='value',
        color=alt.Color('variable', legend=None),
        tooltip=['index', 'variable', 'value']
    ).properties(
        width=600,
        height=400
    )
    st.subheader("Pairwise Cosine Similarity Matrix (Visualization)")
    st.altair_chart(chart, use_container_width=True)

    # Find the most similar tweet for each tweet
    st.subheader("Most Similar Tweets")
    for i, tweet in enumerate(tweets):
        st.write(f"Most similar to tweet {i+1}:")
        most_similar = np.argsort(cosine_sim[i])[::-1][1]
        st.write(f"- Tweet {most_similar+1}: {tweets[most_similar]}")

if __name__ == "__main__":
    app()
