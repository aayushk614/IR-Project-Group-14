
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np



def find_similarity(tweet_list):

    # Initialize the count vectorizer
    vectorizer = CountVectorizer().fit_transform(tweet_list)

    # Calculate the cosine similarity between all pairs of sentences
    cosine_similarities = cosine_similarity(vectorizer)

    # Print the results
    # for i in range(len(tweet_list)):
    #     for j in range(i+1, len(tweet_list)):
    #         print(f"Cosine similarity between '{tweet_list[i]}' and '{tweet_list[j]}': {cosine_similarities[i][j]}")
    

    return cosine_similarities


# Define cosine similarity function
def cosine_similarity_new(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)


def find_similarity_vec(tweet_list):

    # Initialize the count vectorizer
    vectorizer = CountVectorizer().fit_transform(tweet_list)
    X = vectorizer
    X = X.toarray()

    # Calculate pairwise cosine similarity
    n_tweets = len(tweet_list)
    cosine_sim = np.zeros((n_tweets, n_tweets))
    for i in range(n_tweets):
        for j in range(n_tweets):
            cosine_sim[i][j] = cosine_similarity_new(X[i], X[j])


    return cosine_sim
