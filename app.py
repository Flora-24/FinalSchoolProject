from flask import Flask
from flask import jsonify
from flask import request

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


from flask_cors import CORS
# CORS(app)


app = Flask(__name__)

@app.route('/')
def hello():
    return "How are you!"

if __name__ == '__main__':
    app.run()

# Create an instance of the SentimentIntensityAnalyzer class
sia = SentimentIntensityAnalyzer()

# Define a function to perform sentiment analysis
def analyze_sentiment(text):
    # Get the sentiment scores for the given text
    sentiment_scores = sia.polarity_scores(text)

    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Return the sentiment and sentiment scores
    return sentiment, sentiment_scores

# Example usage
text = "I am confused"
sentiment, sentiment_scores = analyze_sentiment(text)

print("Text:", text)
print("Sentiment:", sentiment)
print("Sentiment Scores:", sentiment_scores)

@app.route("/sentiment", methods=['GET'])
def hello_world():
    text = request.args.get('text')
    sentiment, sentiment_scores = analyze_sentiment(text) 
    response = jsonify({"sentiment": sentiment, "score": sentiment_scores })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Running app
# if __name__ == '__main__':
#     app.run(debug=True)