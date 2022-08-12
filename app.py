from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import conversate
import re

# Creating the flask app
app = Flask(__name__)
CORS(app) # give cross origin resource sharing capabilities

# Post functionality for the back and forth conversation with the chatbot
@app.post("/answer")
def answer():
    text = request.get_json().get("message")
    # Check user input for a valid alpha request
    if re.search(r'\d', text):
        botAnswer = 'A valid question does not use numbers. Please try again.'
    else:
        botAnswer = conversate(text)
    ansDict = {"answer": botAnswer}
    return jsonify(ansDict) # Return chatbot answer in a JSON

if __name__ == "__main__":
    app.run()