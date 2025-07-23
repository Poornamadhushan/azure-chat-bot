:\Edubot\azure-chat-bot\README.md
# Azure Chat Bot

A simple web-based chatbot using Azure OpenAI and Flask.

## Features

- Chat with an AI assistant powered by Azure OpenAI.
- Simple web interface.
- Easily customizable.

## Requirements

- Python 3.8+
- Flask
- openai

## Setup

1. **Clone the repository**  
   Download or clone this repository to your local machine.

2. **Install dependencies**
   ```
   pip install flask openai
   ```

3. **Set your Azure OpenAI credentials**  
   Set the following environment variables or edit them in `app.py`:
   - `ENDPOINT_URL`
   - `DEPLOYMENT_NAME`
   - `AZURE_OPENAI_API_KEY`

4. **Run the server**
   ```
   python app.py
   ```

5. **Open the chat interface**  
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.