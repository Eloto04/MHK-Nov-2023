import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "API_KEY_HERE" # insert API key in quotes
client = OpenAI()
chatlog = []

print("Welcome to the bootleg chatbot! Respond with 'q' or 'Q' at any time to quit.")
system_role = input("\nTell the system how to respond during this conversation (i.e. 'You will respond in poetic form.'). Otherwise, press Enter.\n")
if system_role == "q" or system_role == "Q":
    exit()
chatlog.append({"role": "system", "content": system_role})

while True:
    user_prompt = input("\nAsk the system a question (i.e. 'How do I integrate a function?').\n")
    if user_prompt == 'q' or user_prompt == 'Q':
      exit()
    chatlog.append({"role": "user", "content": user_prompt})
    print("\nBot response loading...")

    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatlog
        )
    
    chatlog.append(completion.choices[0].message)
    print(completion.choices[0].message.content)


