import json
from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore
import os

app = Flask(__name__)
CORS(app)

# Path to the JSON file where the token will be stored
json_file_path = 'token_data.json'

# Helper function to save token to JSON file
def save_token_to_json(token):
    # If file exists, load existing data, otherwise start with an empty dict
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # Update the JSON with the new token, removing extra quotes
    data['token'] = token.strip('"')

    # Write updated data back to the file
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/storeToken', methods=['POST'])
def store_token():
    data = request.get_json()
    token = data.get('token')
    
    if token:
        # Save the token to the JSON file after stripping extra quotes
        save_token_to_json(token)
        # Assign the stripped token to a variable first
        stripped_token = token.strip('"')

        # Then use the variable in the f-string
        print(f"Received and saved token: {stripped_token}")


        return jsonify({"status": "success"})
    return jsonify({"status": "failure"}), 400

if __name__ == "__main__":
    app.run(debug=True)
