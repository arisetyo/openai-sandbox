'''
An example of using OpenAI to analyze an image.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

image_url = "https://static1.straitstimes.com.sg/s3fs-public/styles/large30x20/public/articles/2021/09/26/mi_koeyeet_260921.jpg"

# Load environment variables from .env file
load_dotenv()

# create openAI client
client = OpenAI(
  organization=os.getenv('OPENAI_ORGANIZATION'),
  project=os.getenv('OPENAI_PROJECT_NAME'), # project name: "Belajar OpenAI"
  api_key=os.getenv('OPENAI_API_KEY')
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    # tell the model that the user is asking a for an image analysis
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": image_url,
          },
        },
      ],
    },
  ]
)

# print the completion
# here we wait for the whole completion to be generated, instead of streaming it in chunks
output = response.choices[0].message.content
print(output)
