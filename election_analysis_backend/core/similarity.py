from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np






# Define the sentences to compare
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The lazy dog is jumped over by a quick brown fox",
    "I like to eat pizza",
    "Pizza is my favorite food",
    "The quick brown fox ate pizza"
]

# # Initialize the count vectorizer
# vectorizer = CountVectorizer().fit_transform(sentences)

# # Calculate the cosine similarity between all pairs of sentences
# cosine_similarities = cosine_similarity(vectorizer)

# # Print the results
# for i in range(len(sentences)):
#     for j in range(i+1, len(sentences)):
#         print(f"Cosine similarity between '{sentences[i]}' and '{sentences[j]}': {cosine_similarities[i][j]}")


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