import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers ={
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {api_key}"
}

data = {
    "model" : "llama-3.3-70b-versatile",
    "messages" : [
        {
            "role": "user",
            "content": "text = apple * 500"
                }
    ]
}

request = requests.post(url, headers=headers, json=data)

print(request.status_code)
print(request.json())