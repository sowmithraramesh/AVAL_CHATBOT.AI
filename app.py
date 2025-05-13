from flask import Flask, jsonify, request
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Initialize the chatbot
chatbot = ChatBot('Aval.AI - PCOS Wellness')

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train with built-in English corpus
trainer.train('chatterbot.corpus.english')

# Train with custom PCOS data (your YAML file)
trainer.train('C:/Users/sowmi/OneDrive/Desktop/AVAL.AI/pcos_data.yml')

# Endpoint for chatbot response
@app.route("/get", methods=["GET", "POST"])
def get_response():
    user_input = request.args.get('user_input')  # Get user input from query parameter
    response = chatbot.get_response(user_input)
    return jsonify({'response': str(response)})

if __name__ == "__main__":
    app.run(debug=True)
