import random
from flask import Flask
from flask import jsonify
from flask import request
import requests

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask_cors import CORS


app = Flask(__name__)
quotes = [{
    "text": "I deserve to be with someone who will make the rest of my life the best of my life",
    "author": "Abraham Lincoln",
    "type": "Positive"
  },
  {
    "text": "Difficulties increase the nearer we get to the goal.",
    "author": "Johann Wolfgang von Goethe",
    "type": "Negative"
  },
  {
    "text": "Fate is in your hands and no one elses",
    "author": "Byron Pulsifer",
    "type": "Neutral",
  },
  {
    "text": "I love starting my day with one thing i am thankful for.",
    "author": "Lao Tzu",
    "type": "Positive",
  },
 
  {
    "text": "I only give my energy to things that add to my growth",
    "author": "Aristotle",
    "type": "Negative",
  },
  {
    "text": "Life is a learning experience, only if you learn.",
    "author": "Yogi Berra",
    "type": "Negative",
  },
  {
    "text": "It is okay to hurt yourself. Just learn from your mistakes",
    "author": "Margaret Sangster",
    "type": "Negative",
  },
  {
    "text": "Peace comes from within. Do not seek it without.",
    "author": "Buddha",
    "type": "Negative",
  },
  {
    "text": "I am working on me for me",
    "author": "Byron Pulsifer",
      "type": "Positive",
  },
  {
    "text": "We can only learn to love by loving.",
    "author": "Iris Murdoch",
    "type": "Positive",
  }
  ]  # List to store the quotes

CORS(app)


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


# Example usage in backend
text = ""
sentiment, sentiment_scores = analyze_sentiment(text)

print("Text:", text)
print("Sentiment:", sentiment)
print("Sentiment Scores:", sentiment_scores)


@app.route("/sentiment", methods=['GET'])
def get_sentiment():
    text = request.args.get('text')
    sentiment, sentiment_scores = analyze_sentiment(text)
    response = jsonify({"sentiment": sentiment, "score": sentiment_scores})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/quotes', methods=['GET'])
def handle_quotes():
    sentiment = request.args.get('sentiment')
    filtered_quotes = [ quote for quote in quotes if quote["type"] == (str(sentiment)).strip()]
    
    quote = random.choice(filtered_quotes)
    if quote:
        return jsonify(quote)
    else:
        return jsonify({"error": "some error occured"}), 400
    
      


# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3001', debug=True)
