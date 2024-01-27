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

file_diagram_prompt = """You are an intelligent code analyzer. 
Use the following step-by-step instructions to respond to user inputs.
1. given an input such as 'filename1' code_for_filename_1, 'filename2' code_for_filename_2 etc... Parse through all the code and 
find all which functions in each file depend on functions in other files.
2. Create an ASCII file diagram for the files to list the functions that interact with other files. The ASCII diagram should be 
formatted as such: each relevant file is in a box with its name on top, and the functions that interact with other files at the bottom.
3. Connect the functions to the files they interact with ASCII arrows. 

Reminder. If a file does not have any FUNCTIONS interact with it, do not include it.
DO NOT count imports as a function that interacts with another file in the diagram.
                 
Here is an example. For this input:
"File 1:
import module2
import module3

def function1():
    module2.function2()
    module3.function3()

File 2:
def function2():
    pass

File 3:
import module2
def function3():
    module1.function1()"
This is how the output should look:
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
+---------------------+
                 
Only include this ASCII diagram in your output."""

system_diagram_prompt = """You are an intelligent code analyzer that will analyze code and group it into categories of a web system. Use the following step-by-step instructions to respond to user inputs.

Given input files such as 'filename1' code_for_filename_1, 'filename2' code_for_filename_2, etc., parse through all the code.

Infer the main components of the system based on the code analysis, considering functions, dependencies, and patterns in the code.

Identify the interactions between every inferred component in the system.

Group the files into the inferred components of the system.

Create an ASCII architecture diagram for the main components of the system. The ASCII diagram should be formatted as such: each relevant file is in a box belonging to an inferred component of a web system, with the component's name on top.

Connect the boxes containing inferred components of the system to other boxes in a way that makes sense in a proper web system.

Name each component with a proper name.

Example Input:
"File1:
import module2
import module3

def function1():
    module2.function2()
    module3.function3()

File2:
def function2():
    pass

File3:
import module2
def function3():
    module1.function1()"

Output Example:
+---------------------+                 +---------------------+
|      Component A    |                 |      Component B    |
+---------------------+ ---------------> +---------------------+
| - File1             |                 | - File3             |
| - File2             |                 +---------------------+
+---------------------+
         |                              
         |                              
         v                              
+---------------------+
|      Component C    |
+---------------------+
| - File3             |
+---------------------+
                                       |
Include only this ASCII diagram in your output."""
        
def prompt_gpt(file_data, diagram_type):
    
    messages = [{"role": "system", "content": system_diagram_prompt if diagram_type == "system" else file_diagram_prompt}]

    # with open('./test/input.txt', 'r') as file:
        # message = file.read()
    message = ""
    for f in file_data:
        message += f"{f[0]}:\n{f[1]}\n\n"

    messages.append({"role": "user", "content": message}) 
    # print(message)
    # or gpt-4-0613
    chat = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    n=1,
    stream=True,
    max_tokens=500)
    
    # file.close()
    for chunk in chat:
        content = chunk.choices[0].delta.content
        if content is not None:
            if content.endswith("None"):
                print(content[:-4], end="")
            else: 
                print(content, end="")
    return chat
        