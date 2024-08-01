# textblob library

# let import TextBlob over  here in the app
from textblob import TextBlob
# create a sample text

texts =[
    "I love NLP !it's works great and i'm very satisfied",
    "this is my first experience on doing sentiment analysis",
    "The NLP sentiment analysis is quiet intresting it is neither good or bad",
]

# create function to do the sentiment analysis
def analyze_sentiment(text):
    analysis =TextBlob(text)
    #-1.0 - 1.0 polarity score 
    polarity = analysis.sentiment.polarity
    if polarity >0:
        sentiment="Positive"
    elif polarity<0:
         sentiment="negative"
    else:
        sentiment="Neutral"
    return sentiment
for text in texts:
    sentiment =analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"Sentiment:{sentiment}\n")