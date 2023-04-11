import streamlit as st
import pandas as pd
from htbuilder import div, styles

from collections import defaultdict, namedtuple
from htbuilder import div, big, h2, styles
from htbuilder.units import rem
from math import floor
from textblob import TextBlob
import altair as alt

from tweet_list import fetch_tweet
from analyze_tweets import analyze_tweets as func1

st.set_page_config(page_title="Sentiment Summarizer")

st.write('<base target="_blank">', unsafe_allow_html=True)


a, b = st.columns([1, 10])

with a:
    st.text("")
    st.image("logo.png", width=50)
with b:
    st.title("Twitter Sentiment Analyzer")

st.write("This page shows the sentiment summary of the fetched tweets from previous homepage.")


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



# with st.form(key="my_form"):



# @st.cache_resource
# def initial_setup():
#     from textblob.download_corpora import download_all
#     download_all()
#     import nltk
#     nltk.download('punkt')

# initial_setup()




COLOR_RED = "#FF4B4B"
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

def display_dict(dict):
    for k, v in dict.items():
        a, b = st.columns([1, 4])
        a.write(f"**{k}:**")
        b.write(v)



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

    SentimentListItem = namedtuple(
        "SentimentListItem", ( "polarity", "subjectivity", "text")
    )

    for tweet in tweets:
        clean_text = tweet
        blob = TextBlob(clean_text)

        add_counts(word_counts, blob.word_counts)
        add_counts(bigram_counts, get_counts(blob.ngrams(2), key_sep=" "))
        add_counts(trigram_counts, get_counts(blob.ngrams(3), key_sep=" "))
        sentiment_list.append(
            SentimentListItem(
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
        "nounphrase_counts": to_df(nounphrase_counts),
        "sentiment_list": sentiment_list,
    }



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

tweets1 = fetch_tweet()

results = func1(tweets1)

# --------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------
# Draw results

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


with st.expander("ℹ️ How to interpret the results", expanded=False):
    st.write(
        """
        **Polarity**: Polarity is a float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement
        **Subjectivity**: Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1].
        And make sure to 👆 click on datapoints above to see the actual tweet!
        """
    )
    st.write("")


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


