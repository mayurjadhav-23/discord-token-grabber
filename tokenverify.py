import json
import requests

# Function to read the token from the JSON file
def get_token_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            return data.get('token')  # Return the token from the JSON
    except FileNotFoundError:
        print(f"Error: {json_file_path} file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: JSON is invalid or cannot be decoded.")
        return None

# Function to check if the token is valid
def check_token(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": token  # Use the token directly, no 'Bearer' for user tokens
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        print("Token is valid!")
        print("User info:", user_info)
    else:
        print(f"Token is invalid or expired: {response.status_code}, {response.text}")

# Define the path to your JSON file
json_file_path = 'token_data.json'

# Fetch the token from the JSON file
token = get_token_from_json(json_file_path)

# Check if the token was successfully retrieved
if token:
    check_token(token)
else:
    print("No valid token found.")
