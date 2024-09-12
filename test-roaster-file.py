'''
Create a Python script that roast a screenshot of IG feed.

WORK IN PROGRESS
'''

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
parser.add_argument('--ss', type=str, required=True, help='screenshot name')
# Parse arguments
args = parser.parse_args()
# Assign the user request to the variable
screenshot_file = args.ss

# Upload the image to OpenAI
with open(screenshot_file, 'rb') as file:
    image_file = client.files.create(file=file, purpose='fine-tune')

# Get the file ID from the response
file_id = image_file.id

# get roasting from OpenAI
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": "You are a sassy judgmental internet celebrity who roasts other people's Instagram feeds."
    },
    # tell the model that the user is asking a for an image analysis
    {
      "role": "user",
      "content": "Roast the IG feed in this screenshot",
      "attachments": [
        {
          "type": "image",
          "file_id": file_id,  # Use the file ID
        },
      ],
    },
  ],
  max_tokens=200
)

# print the completion
# here we wait for the whole completion to be generated, instead of streaming it in chunks
output = response.choices[0].message.content
print(output)
