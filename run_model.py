import os
from openai import AzureOpenAI

# Environment variables or defaults
endpoint = os.getenv("ENDPOINT_URL", "https://devnoxbot.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "devnoxbot")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "api_key_placeholder")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Chat prompt
messages = [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
    },
    {
        "role": "user",
        "content": "I am going to Paris, what should I see?"
    },
    {
        "role": "assistant",
        "content": "Paris, the capital of France, is known for its stunning architecture, art museums, historical landmarks, and romantic atmosphere. Here are some top attractions:\n\n1. Eiffel Tower\n2. Louvre Museum\n3. Notre-Dame Cathedral"
    },
    {
        "role": "user",
        "content": "What is so great about #1?"
    }
]

# Generate the completion
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

# Print full response
print("\nAssistant Response:\n")
print(completion.choices[0].message.content)
