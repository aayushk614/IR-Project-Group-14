
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import pandas as pd
import textblob

from textblob import TextBlob
# Load NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define text preprocessing functions
def preprocess_tweet(tweet):
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Perform stemming
    ps = PorterStemmer()
    tokens = [ps.stem(token) for token in tokens]
    
    # Join tokens back into a single string
    preprocessed_tweet = ' '.join(tokens)
    
    return preprocessed_tweet

# Create a Streamlit app
def main():
    # Set app title
    st.title('Tweet Manipulation Classifier')
    
    # Input text box for user input
    tweet = st.text_input('Enter a tweet:')
    
    # Preprocess the input tweet
    preprocessed_tweet = preprocess_tweet(tweet)
    tweet_list=[preprocessed_tweet]
    new_tweet_sentiment = pd.DataFrame({'polarity': [TextBlob(tweet).sentiment.polarity for tweet in tweet_list], 'subjectivity': [TextBlob(tweet).sentiment.subjectivity for tweet in tweet_list]})
    new_tweet_pred = model.predict(new_tweet_sentiment)
    
    
    # Make prediction button
    if st.button('Predict'):
        prediction = 0
        #print('Predicted labels for new tweets:', new_tweet_pred)
        # Make prediction using the trained model
        if new_tweet_pred == "['authentic']":
            prediction = 1
        
        #Display prediction result
        if prediction == 1:
            st.write('This tweet is classified as manipulated.')
        else:
            st.write('This tweet is classified as not manipulated.')

# Run the Streamlit app
if __name__ == '__main__':
    main()



