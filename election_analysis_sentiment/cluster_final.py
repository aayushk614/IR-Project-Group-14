import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from pytagcloud import create_tag_image, make_tags

from collections import Counter
from pytagcloud import create_tag_image, make_tags
from tweet_list import fetch_tweet
from pytagcloud.lang.counter import get_tag_counts

st.set_page_config(page_title="Tweet Clustering and Analysis", page_icon=":mag:", layout="wide")


tweets = fetch_tweet()


# Preprocess the tweets
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(tweets)
X = X.toarray()

# Define number of clusters
n_clusters = st.sidebar.slider("Select the number of clusters:", min_value=2, max_value=10, value=3, step=1)

# Define KMeans clustering model
model = KMeans(n_clusters=n_clusters, random_state=42)
model.fit(X)

# Get cluster labels and assign each tweet to a cluster
labels = model.labels_
clustered_tweets = {}
for i, label in enumerate(labels):
    if label in clustered_tweets:
        clustered_tweets[label].append(tweets[i])
    else:
        clustered_tweets[label] = [tweets[i]]

# Define cosine similarity function
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Calculate pairwise cosine similarity for each cluster
cosine_sim_clusters = {}
for i in range(n_clusters):
    cluster_tweets = clustered_tweets[i]
    n_tweets = len(cluster_tweets)
    cluster_X = vectorizer.transform(cluster_tweets)
    cluster_X = cluster_X.toarray()
    cosine_sim = np.zeros((n_tweets, n_tweets))
    for j in range(n_tweets):
        for k in range(n_tweets):
            cosine_sim[j][k] = cosine_similarity(cluster_X[j], cluster_X[k])
    cosine_sim_clusters[i] = cosine_sim

# Define Streamlit app
def app():

    # Display the tweet text and their assigned clusters
    st.title("Tweet Clustering and Analysis")
    st.subheader("Tweet Text and Clusters")
    tweet_col, cluster_col = st.columns((1,1))
    with tweet_col:
        for i, tweet in enumerate(tweets):
            st.write(f"{i+1}. {tweet}")
    with cluster_col:
        for i, label in enumerate(labels):
            st.write(f"{i+1}. Cluster {label+1}")


# Display the most common words in each cluster

    st.subheader("Most Common Words in Each Cluster")
    for i in range(n_clusters):
        cluster_tweets = clustered_tweets[i]
        # Concatenate the tweets into a single string
        cluster_text = ' '.join(cluster_tweets)
        # Get the tag counts for the cluster text
        tags = make_tags([(tag, count) for tag, count in Counter(cluster_text.split()).items()])
        create_tag_image(tags, f"cluster_{i+1}.png", size=(600, 400), fontname='Lobster')
        st.image(f"cluster_{i+1}.png")




if __name__ == '__main__':
    app()