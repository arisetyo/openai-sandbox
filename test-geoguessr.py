'''
Create a Python script + OpenAI library that guess the location of a screenshot.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# create openAI client
client = OpenAI(
  organization=os.getenv('OPENAI_ORGANIZATION'),
  project=os.getenv('OPENAI_PROJECT_NAME'),
  api_key=os.getenv('OPENAI_API_KEY')
)

# screenshot_url = 'https://asset-2.tstatic.net/jabar/foto/bank/images/lalu-lintas-di-jalan-wastukencana-bandung_20171226_165550.jpg'
# screenshot_url = 'https://img.antaranews.com/cache/1200x800/2022/07/21/FB_IMG_1658387830775.jpg.webp'
# screenshot_url = 'https://a.travel-assets.com/findyours-php/viewfinder/images/res40/26000/26297-Nairobi.jpg'
# screenshot_url = 'https://www.tierrasvivas.com/img/capital-of-peru-06-1076.jpg'
# screenshot_url = 'https://www.thenatureofcities.com/TNOC/wp-content/uploads/2018/07/Feature.jpg'
# screenshot_url = 'https://upload.wikimedia.org/wikipedia/commons/e/ea/Wellington_Street_construction.jpg'
screenshot_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Rue_pi%C3%A9tonne_centre_de_Perth.JPG/2560px-Rue_pi%C3%A9tonne_centre_de_Perth.JPG'

# get answer from OpenAI
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": "You are an expert 'Geoguessr'. You have an extensive knowledge on various locations around the world, supported by your amazing knowledge of environmental biology, geography, traffic laws, history, linguistic, and culture."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Guess the location shown in this screenshot. Gives as much detail as possible and list the factors that made you come to the decision. Give a final conclusion on the location."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": screenshot_url,
          },
        },
      ],
    },
  ],
  max_tokens=480
)

# print the response
output = response.choices[0].message.content
print(output)
