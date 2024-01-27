import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
api_key = os.getenv('GPT_KEY')

def main():
    # Initialize chat history
    messages = [{"role": "system", "content": "You are an intelligent code analyzer. \
                Given an input formatted as such: 'filename1' code_for_filename_1, 'filename2' code_for_filename_2 etc... \
                You can generate code dependencies to see how the files interact with each other\
                and create ASCII diagrams for code interactions."}]

    message = input("User : ")
    
    # If message contains exit command, then stop the loop
    if message.lower() == 'exit':
        return
    if message: 
        messages.append({"role": "user", "content": message}) 
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 
        
        reply = chat.choices[0].message.content 
    
        print(f"ChatGPT: {reply}") 
        messages.append({"role": "assistant", "content": reply}) 
        return reply
    # Exit message
    print("Exited the chat.")