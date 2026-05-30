import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key = api_key, 
)
chat_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain what a transformer is in 3 sentences."
        }]
    )
print(chat_response.choices[0].message.content)