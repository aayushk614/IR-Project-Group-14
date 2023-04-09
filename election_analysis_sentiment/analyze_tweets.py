import numpy as np
import pandas as pd
import streamlit as st
from collections import defaultdict, namedtuple
from textblob import TextBlob


@st.cache_resource
def initial_setup():
    from textblob.download_corpora import download_all
    download_all()
    import nltk
    nltk.download('punkt')


# Uncomment if there is a NLTK error and rerun.
# initial_setup()



def add_counts(accumulator, ngrams):
    for ngram, count in ngrams.items():
        accumulator[ngram] += count

def get_counts(blobfield, key_sep):
    return {key_sep.join(x): blobfield.count(x) for x in blobfield}


def analyze_tweets(tweets):  

    word_counts = defaultdict(int)
    bigram_counts = defaultdict(int)
    trigram_counts = defaultdict(int)
    nounphrase_counts = defaultdict(int)
    sentiment_list = []

    SentimentList = namedtuple(
        "SentimentList", ( "polarity", "subjectivity", "text")
    )

    for tweet in tweets:
        clean_text = tweet
        blob = TextBlob(clean_text)

        add_counts(word_counts, blob.word_counts)
        add_counts(bigram_counts, get_counts(blob.ngrams(2), key_sep=" "))
        add_counts(trigram_counts, get_counts(blob.ngrams(3), key_sep=" "))
        sentiment_list.append(
            SentimentList(
                blob.sentiment.polarity,
                blob.sentiment.subjectivity,
                tweet,
            )
        )

    def to_df(the_dict):
        items = the_dict.items()
        items = ((term, count, len(term.split(" "))) for (term, count) in items)
        return pd.DataFrame(items, columns=("term", "count", "num_words"))

    return {
        "word_counts": to_df(word_counts),
        "bigram_counts": to_df(bigram_counts),
        "trigram_counts": to_df(trigram_counts),
        "sentiment_list": sentiment_list,
    }

