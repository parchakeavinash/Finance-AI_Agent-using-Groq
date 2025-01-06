import os
from groq import Groq

client = Groq(
    api_key=os.environ.get(""),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the meaning of Avinash in Sanskrit?",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)