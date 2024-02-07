import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the API endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get the user's input from the JSON request data
        data = request.get_json()
        user_input = data['message']

        # Replace 'AIzaSyBuhnVhACUyBRxbv7zTIoFunnW5GT9Y3GA' with the actual chatbot API URL
        chatbot_api_url = 'AIzaSyBuhnVhACUyBRxbv7zTIoFunnW5GT9Y3GA'  # Replace with the actual chatbot API URL
        headers = {'Content-Type': 'application/json'}

        # Send the user's input to the chatbot API using the requests library
        body = {'message': user_input}
        response = requests.post(chatbot_api_url, headers=headers, json=body)

        # Check if the request to the chatbot API was successful
        response.raise_for_status()

        # Parse the chatbot's response
        chatbot_response = response.json()
        chatbot_message = chatbot_response['message']

        # Return the chatbot's response to the user
        return jsonify({'message': chatbot_message})

    except Exception as e:
        # Handle exceptions, log them, and return an error response
        error_message = f"Error: {str(e)}"
        return jsonify({'error': error_message}), 500  # 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
