import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Ask user for input prompt
user_prompt = input("Enter your prompt: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)