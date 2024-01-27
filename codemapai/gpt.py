import os
import sys 
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables first.
load_dotenv()  
api_key = os.getenv('GPT_KEY')

# Then initiate the OpenAI client with the api_key.
client = OpenAI(api_key = api_key)

        

def prompt_gpt(message):
    # Initialize chat history
    messages = [{"role": "system", "content": """You are an intelligent code analyzer. 
Given an input formatted as such: 'filename1' code_for_filename_1, 'filename2' code_for_filename_2 etc... 
You can generate code dependencies to see how the files interact with each other and create ASCII diagrams for
code interactions. In your output, only create an ASCII diagram for the files.
Within each ASCII diagram, only list the functions that interact with other files. 
                DO NOT include any imports/modules in the diagram. I REPEAT DO NOT include any imports/modules in the diagram.
This is an example of how an output should be formatted:
+---------------------+                 +---------------------+
|      File 1         |                 |      File 3         |
+---------------------+ ------------->  +---------------------+
| - File2.function2   |                 | - File3.function3   |
+---------------------+                 +---------------------+
        |                           
        |                          
        |                
        v                  
+---------------------+
|      File 2         |
+---------------------+
| - File1.function1   |
+---------------------+"""}]

    # with open('./test/input2.txt', 'r') as file:
    #     message = file.read()
    messages.append({"role": "user", "content": message}) 
    # or gpt-4-0613
    chat = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages,
    n=1,
    stream=True,
    max_tokens=500)
        
    for chunk in chat:
        print((chunk.choices[0].delta.content), end="")

    messages.append({"role": "assistant", "content": chat}) 
    # return chat
    # TODO: Exit message