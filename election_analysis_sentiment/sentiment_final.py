import streamlit as st
import pandas as pd
from htbuilder import div, styles
import numpy as np
import pandas as pd
import altair as alt
from sklearn.feature_extraction.text import CountVectorizer

from htbuilder import div, big, h2, styles
from htbuilder.units import rem
from math import floor
from textblob import TextBlob
import altair as alt

from tweet_list import fetch_tweet, retrieve_tweet
from analyze_tweets import analyze_tweets

st.set_page_config(page_title="Sentiment Summarizer")

st.write('<base target="_blank">', unsafe_allow_html=True)

a, b = st.columns([1, 10])

with a:
    st.text("")
    st.image("logo.png", width=50)
with b:
    st.title("Twitter Sentiment Analyzer")

st.write("This page shows the sentiment summary of the fetched tweets from previous homepage.")

def test_app(tweetlist):

    with st.expander("ℹ️ How to Interpret the results", expanded=False):

        st.markdown(
            """
            ### Polarity
            Polarity is a float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement.
            """
        )

        st.markdown(
            """
            ### Subjectivity
        Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1].
            """
        )

        st.markdown(
            """
            """
        )


    st.write("")

    # @st.cache_resource
    # def initial_setup():
    #     from textblob.download_corpora import download_all
    #     download_all()
    #     import nltk
    #     nltk.download('punkt')

    # initial_setup()

    COLOR_BLUE = "#1C83E1"
    COLOR_CYAN = "#00C0F2"



    def display_dial(title, value, color):
        st.markdown(
            div(
                style=styles(
                    text_align="center",
                    color=color,
                    padding=(rem(0.8), 0, rem(3), 0),
                )
            )(
                h2(style=styles(font_size=rem(0.8), font_weight=600, padding=0))(title),
                big(style=styles(font_size=rem(3), font_weight=800, line_height=1))(
                    value
                ),
            ),
            unsafe_allow_html=True,
        )

 

    # --------------------------------------------------------------------------------------------------

    tweets = ["congress made vemula nation talk point even though doubt case amp vemula dalit itself stop bjp make ramalingam case attain nation scale amp chang dalit discours take one remark pm modi make happen",
    "bjp win battl past month bengal pm modi arriv win biggest battl announc warcri upcom war tmc elect modisonarbangla",
    "inclusivemind ark bjpindia rahul gandhi bjp think cellchatumediacroniesscrit writer andbhakt crore speach give victori then late atal bihari vajpeyi much better shine india",
    "senior congress leader manishtewari jpc definit next parliament parallel crimin investig process go go away rafal rafalenot",
    "bc congress take kickback fr pp",
    "rahul lie caught exclus former defenc secretari g mohan kumar tear rahul gandhi lie say no pmo interfer rafal price",
    "expect meltdown congress elect wait till februari end bahut saar possibl hain ji",
    "stori realli expos develop propaganda nation congress cudnt yrs modi sirji ask month abl hear terrifi stori jharkhand govt cudnt even solv basic issu last yrs",
    "issu problem parrikar say defenc secretari resolv problemmatt princip secretari pm actual nail modi anyth els",
    "forthefirsttim activ diplomaci pm modi india emerg leader intern platform first indian prime minist visit israel strengthen tie ageold natur alli year",
    "modiunstopp speech made noisi kharg amp compani nervous confid speak way come easili one sincer amp honest job paplu taplu remain absent perhap nirmala ji arunji piyush ji s trailer prefer avoid modi ji s punch",
    "piti state affair swachh bharat mission modi s kashi could understood fact even minist neelkanth tiwari also admit work mark flopswachhbharat",
    "jim jordan remain best argument drug test member congress whitakerhear",
    "rahul rahul gandhi ji use claim defenc minist manoharparrikar ji complet ignor rafaled note rafal file anoth lie expos rahulliecaught",
    "modi govt make kitchen smoke free pmuy approx crore lpg connect provid poor india becom second largest lpg consum lpg coverag cleaner fuel ensur cleaner environ too transformingindia",
    "bjp mp sh ianuragthakur launch campaign abkibaarpaar",
    "prime minist shri modi today expos congress parti s fals fake campaign sever issu deliv outstand speech floor lok sabha congratul prime minist complet demolish opposit s claim",
    ]

    #tweets1 = tweetlist 

    results = analyze_tweets(tweetlist)


    st.write("## Sentiment from the most recent ", len(tweets)," tweets")


    # fetching sentiment results

    sentiment_df = pd.DataFrame(results["sentiment_list"])

    polarity_color = COLOR_BLUE
    subjectivity_color = COLOR_CYAN

    a, b = st.columns(2)

    with a:
        display_dial("POLARITY", f"{sentiment_df['polarity'].mean():.2f}", polarity_color)
    with b:
        display_dial(
            "SUBJECTIVITY", f"{sentiment_df['subjectivity'].mean():.2f}", subjectivity_color
        )



    st.markdown("## Top terms")

    terms = pd.concat(
        [
            results["word_counts"],
            results["bigram_counts"],
            results["trigram_counts"],
        ]
    )

    a, b = st.columns(2)
    adjustment_factor = a.slider("Prioritize long expressions", 0.0, 1.0, 0.2, 0.001)

    max_threshold = terms["count"].max()
    threshold = b.slider("Threshold", 0.0, 1.0, 0.3) * max_threshold

    weights = (terms["num_words"] * adjustment_factor * (terms["count"] - 1)) + terms[
        "count"
    ]

    filtered_terms = terms[weights > threshold]

    st.altair_chart(
        alt.Chart(filtered_terms)
        .mark_bar(tooltip=True)
        .encode(
            x="count:Q",
            y=alt.Y("term:N", sort="-x"),
            color=alt.Color(value=COLOR_BLUE),
        ),
        use_container_width=True,
    )

    with st.expander("Show raw data", expanded=False):

        st.markdown("## Raw data")
        st.markdown("")

        def draw_count(label, df, init_filter_divider):
            xmax = int(floor(df["count"].max()))
            x = st.slider(label, 0, xmax, xmax // init_filter_divider)
            df = df[df["count"] > x]
            df = df.sort_values(by="count", ascending=False)
            df
            " "

        if st.checkbox("Show term counts"):
            draw_count("Term count cut-off", terms, 5)

        if st.checkbox("Show word counts"):
            draw_count("Word count cut-off", results["word_counts"], 5)

        if st.checkbox("Show bigram counts"):
            draw_count("Bigram count cut-off", results["bigram_counts"], 3)

        if st.checkbox("Show trigram counts"):
            draw_count("Trigram count cut-off", results["trigram_counts"], 2)


    with st.expander("Cosine similarity", expanded=False):

        st.markdown("## Tweet Similarity Analysis")

        tweets = tweetlist

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
        
        
        #st.set_page_config(page_title="Tweet Similarity Analysis")

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




def main():
    user_input = st.text_input("Enter the hashtag:")
    #list = retrieve_tweet(user_input)

    
    if st.button("Submit"):
        list = fetch_tweet()
        test_app(list)

if __name__ == '__main__':
    main()
