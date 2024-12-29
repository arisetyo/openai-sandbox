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
parser.add_argument('--city', type=str, required=True, help='enter a city name')
# Parse arguments
args = parser.parse_args()
# Assign the user request to the variable
city_name = args.city

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a helpful assistant knowledgeable in geography and world history."
    },
    {
      "role": "user",
      "content": "Provide a day-to-day activity for a tourist visiting {} for 3 days. Important: return the answer in a JSON array format.".format(city_name)
    },
  ]
)

output = completion.choices[0].message.content
print(output)

# Example usage:
# python test-itinerary.py --city "New York"
