# •Chatbot Gemini

Chatbot Gemini is a web-based application that utilizes the Gemini API to provide an interactive chatbot experience. Users can input text prompts and optionally upload images to receive generated responses.


# •Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd chatbot-gemini
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy the `.env.example` file to `.env` and replace `<your_gemini_api_key>` with your actual Gemini API key.
   ```
   cp .env.example .env
   ```

# •Usage

1. **Run the application:**
   ```
   python app.py
   ```

2. **Access the chatbot:**
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Interact with the chatbot:**
   - Enter your question in the text area.
   - Optionally, upload an image.
   - Click the "Enviar" button to submit your query.

# •Files Overview

- **app.py**: Main application file that sets up the Flask server and handles chat requests.
- **requirements.txt**: Lists the required Python packages for the project.
- **.env.example**: Template for environment variables, including the GEMINI_API_KEY.
- **utils/gemini_api.py**: Contains the `call_gemini` function for interacting with the Gemini API.
- **static/style.css**: CSS styles for the chatbot interface.
- **templates/index.html**: HTML template for the chatbot interface.

# •License

This project is licensed under the MIT License. See the LICENSE file for more details.