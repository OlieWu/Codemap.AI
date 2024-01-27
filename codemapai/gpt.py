import os
import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
api_key = os.getenv('GPT_KEY')

def prompt_gpt():
    messages = [ {"role": "system", "content":  
                "You are a intelligent assistant for a dev tools feature. The feature includes the following: \
                The user will give you a series of code and the file names. Then, you will do stuff with it "} ] 
    while True: 
        message = input("User : ") 
        if message: 
            messages.append( 
                {"role": "user", "content": message}, 
            ) 
            chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=messages 
            ) 
        reply = chat.choices[0].message.content 
        print(f"ChatGPT: {reply}") 
        messages.append({"role": "assistant", "content": reply}) 