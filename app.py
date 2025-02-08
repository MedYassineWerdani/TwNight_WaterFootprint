from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Autoriser les requêtes depuis Angular

API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not API_KEY:
    raise ValueError("Missing API Key. Set OPENROUTER_API_KEY in environment variables.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    water_footprint_prompt = f"Calculate water footprint based on input: {data}"

    try:
        completion = client.chat.completions.create(
            extra_body={},
            model="google/gemini-2.0-flash-lite-preview-02-05:free",
            messages=[{"role": "user", "content": water_footprint_prompt}]
        )
        
        result = completion.choices[0].message.content
        return jsonify({"water_footprint": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 