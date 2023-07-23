import os
import requests
import json

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"

import openai


# https://conmmunity-openai-4.openai.azure.com/
#

# openai.api_key = os.getenv("AZURE_OPENAI_KEY")
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = "https://conmmunity-openai-4.openai.azure.com/"
openai.RPM = 10

openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name='gpt-4-6' #This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
messages=[
    {"role": "assistant", "content": "The table schema is as follows: "},
    {"role": "user", "content": start_phrase}
          ]

response = openai.ChatCompletion.create(engine=deployment_name, messages=messages, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)