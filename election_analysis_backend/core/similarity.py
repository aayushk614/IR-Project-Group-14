from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np

def find_similarity(tweet_list):
    """
    Calculate the cosine similarity between all pairs of tweets in the given list.

    Args:
        tweet_list (list of str): List of tweets.

    Returns:
        numpy.ndarray: A 2D array containing the cosine similarity scores between all pairs of tweets.
    """
    if not isinstance(tweet_list, list) or not all(isinstance(tweet, str) for tweet in tweet_list):
        raise ValueError("Input must be a list of strings.")

    if len(tweet_list) == 0:
        raise ValueError("Input list must not be empty.")

    # Initialize the count vectorizer
    vectorizer = CountVectorizer().fit_transform(tweet_list)

    # Calculate the cosine similarity between all pairs of sentences
    cosine_similarities = cosine_similarity(vectorizer)

    return cosine_similarities

def cosine_similarity_new(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors.

    Args:
        vec1 (numpy.ndarray): First vector.
        vec2 (numpy.ndarray): Second vector.

    Returns:
        float: Cosine similarity score between the two vectors.
    """
    if not isinstance(vec1, np.ndarray) or not isinstance(vec2, np.ndarray):
        raise ValueError("Input vectors must be numpy arrays.")

    if vec1.shape != vec2.shape:
        raise ValueError("Input vectors must have the same shape.")

    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

def find_similarity_vec(tweet_list):
    """
    Calculate the pairwise cosine similarity between all tweets in the given list.

    Args:
        tweet_list (list of str): List of tweets.

    Returns:
        numpy.ndarray: A 2D array containing the pairwise cosine similarity scores between all tweets.
    """
    if not isinstance(tweet_list, list) or not all(isinstance(tweet, str) for tweet in tweet_list):
        raise ValueError("Input must be a list of strings.")

    if len(tweet_list) == 0:
        raise ValueError("Input list must not be empty.")

    # Initialize the count vectorizer
    vectorizer = CountVectorizer().fit_transform(tweet_list)
    X = vectorizer.toarray()

    # Calculate pairwise cosine similarity
    n_tweets = len(tweet_list)
    cosine_sim = np.zeros((n_tweets, n_tweets))
    for i in range(n_tweets):
        for j in range(n_tweets):
            cosine_sim[i][j] = cosine_similarity_new(X[i], X[j])

    return cosine_sim
