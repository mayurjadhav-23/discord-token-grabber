# Discord Token Grabber

Discord Token Grabber is a Chrome extension that captures Discord user tokens from local storage and sends them to a Flask server for secure storage and verification. The token is then validated against Discord’s API to check its legitimacy. This project is intended for **educational purposes only** to demonstrate client-server communication and token-based authentication processes.

## Features
- Captures Discord user tokens from the browser.
- Sends the token to a Flask server for secure storage.
- Verifies the token using Discord's API.
- Displays user information if the token is valid.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Chrome browser
- (Optional) Node.js and npm for extension development.

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/discord-token-grabber.git

   cd discord-token-grabber
2. **Set up the Flask server:**

    Install the required dependencies:
    ```bash
    pip install Flask flask-cors requests
3. **Run the server:**
    ```bash
    python app.py
4. **Testing the Token Verification:**
    - After grabbing the token, run tokenverify.py to verify its validity using Discord’s API.
   ```bash
   python tokenverify.py
4. **Load the Chrome Extension:**
    - Open Chrome and navigate to chrome://extensions/.
    - Enable Developer Mode.
    - Click "Load unpacked" and select the directory containing the extension files.


## Legal Disclaimer
    This tool is intended solely for educational purposes. The authors of this project are not responsible for any illegal or unethical use of this tool. Misuse of Discord tokens or any unauthorized access to other users' accounts is a violation of Discord’s Terms of Service and applicable laws. Only use this tool in environments where you have explicit permission.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
