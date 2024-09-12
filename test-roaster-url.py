'''
Create a Python script that roast a profile picture from a URL.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

#image_url = "https://pbs.twimg.com/profile_images/1801168482685669376/D8RLEMtN_400x400.jpg"
image_url = "https://pbs.twimg.com/profile_images/1379404366747115527/-Mko4tap_400x400.jpg"
#image_url = "https://pbs.twimg.com/profile_images/1830137947712339969/p9Hy6LNG_400x400.jpg"

# Load environment variables from .env file
load_dotenv()

# create openAI client
client = OpenAI(
  organization=os.getenv('OPENAI_ORGANIZATION'),
  project=os.getenv('OPENAI_PROJECT_NAME'), # project name: "Belajar OpenAI"
  api_key=os.getenv('OPENAI_API_KEY')
)

# get roasting from OpenAI
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": "You are an internet-savvy high-end magazine editor with very sophisticated style and taste, with almost two decades of experience working in various countries and continents."
    },
    # tell the model that the user is asking a for an image analysis
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Roast my profile picture"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": image_url,
          },
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
