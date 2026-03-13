import streamlit as st
from textblob import TextBlob

# App title
st.title("Sentiment Analyzer")

# Input box
review = st.text_input("Enter the Review")

# Button
if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            st.success("Positive")
        else:
            st.error("Negative")

