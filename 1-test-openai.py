import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# create openAI client
client = OpenAI(
  organization=os.getenv('OPENAI_ORGANIZATION'),
  project=os.getenv('OPENAI_PROJECT_NAME'), # project name: "Belajar OpenAI"
  api_key=os.getenv('OPENAI_API_KEY')
)

# Set up argument parser
parser = argparse.ArgumentParser(description='Process some parameters.')
parser.add_argument('--ask', type=str, required=True, help='Ask something to the AI')
# Parse arguments
args = parser.parse_args()
# Assign the user request to the variable
user_request = args.ask

# get completion from OpenAI
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant knowledgeable in geography and world history."},
    {"role": "user", "content": user_request},
  ]
)

# print the completion
output = completion.choices[0].message.content
print(output)

# Example usage:
# python 1-test-openai.py --ask "List the largest cities in the world by population."