from flask import Flask, request, jsonify, send_from_directory
import os
from openai import AzureOpenAI

app = Flask(__name__)

endpoint = os.getenv("ENDPOINT_URL", "https://devnoxbot.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "devnoxbot")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "api_key_placeholder")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

@app.route("/")
def index():
    return send_from_directory(".", "webchat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    messages = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": user_message}
    ]
    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=messages,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stream=False
        )
        response = completion.choices[0].message.content
    except Exception as e:
        response = f"Error: {str(e)}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)