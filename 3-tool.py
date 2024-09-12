'''
An example of calling a function by OpenAI.

https://platform.openai.com/docs/guides/function-calling

STILL NOT WORKING
WORK IN PROGRESS
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

# function to get the result from DATA.txt
def get_result():
  with open('DATA.txt', 'r') as file:
    return file.read()

tools = [
    {
      "type": "function",
      "function": {
        "name": "get_result",
        "description": "Get the score of students. Call this whenever you need to know the exam score of students, for example when someone asks 'What is the exam score of <a student's name>?'",
        "parameters": []
      }
    }
]

messages = [
    {
      "role": "system",
      "content": "You are a teacher who has the exam results stored in the file DATA.txt."
    },
    {
      "role": "user",
      "content": "Hi, can you tell me the exam score of Roger?"
    }
]

# Load environment variables from .env file
load_dotenv()

# create openAI client
client = OpenAI(
  organization=os.getenv('OPENAI_ORGANIZATION'),
  project=os.getenv('OPENAI_PROJECT_NAME'), # project name: "Belajar OpenAI"
  api_key=os.getenv('OPENAI_API_KEY')
)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  tools=tools,
  function_call="auto"  # Auto mode to let the model decide when to call the function
)

# print the completion
# output = response.choices[0]
# print(output)

# Check if the function was called and handle the response
if response.choices[0].finish_reason == "function_call":
  function_name = response.choices[0].message['function_call']['name']
  if function_name == "get_result":
    result = get_result()
    print(result)
else:
  print(response.choices[0].message['content'])