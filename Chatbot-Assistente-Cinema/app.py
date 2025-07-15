import base64
import os
import tempfile
from PIL import Image
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import google.generativeai as generai

load_dotenv()
API_KEY_GEMINAI = os.getenv("API_KEY_GEMINAI")

generai.configure(api_key=API_KEY_GEMINAI)
model = generai.GenerativeModel("gemini-1.5-flash-latest")
chat = model.start_chat(history=[
    {"role": "user", "parts": ['''Você é um assistente virtual especializado cinema, incluindo séries, minisséries, documentários, curta-metragem.
Seu objetivo é fornecer informações precisas e úteis sobre gêneros cinematográficos, direção, elenco, duração, fotografia, prêmios e outras curiosidades sobre esse tema.
Você DEVE recusar educadamente qualquer pergunta que não esteja diretamente relacionada a este tema.
Para perguntas fora do tema, responda algo como: 'Desculpe, mas infelizmente não posso te ajudar com isso. Minha especialidade é falar sobre cinema. ''']},
    {"role": "model", "parts": ["Combinado!"]}
])
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    prompt = request.form.get("prompt", "").strip()
    image = request.files.get("image")

    if not prompt:
        return jsonify({"response": "Faça uma pergunta..."}), 400

    try:
        if image and image.filename:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                image.save(tmp.name)
                pil_image = Image.open(tmp.name)
                response = model.generate_content([prompt, pil_image])
        else:
            response = chat.send_message(prompt)
        text_response = response.text
    except Exception as e:
        text_response = "Desculpe, mas não vou conseguir te ajudar dessa vez."
        print(f"Erro: {e}")

    return jsonify({"response": text_response})

if __name__ == "__main__":
    app.run(debug=True)