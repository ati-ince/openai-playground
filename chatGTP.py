"""
pep8 module info
"""

import configparser

config = configparser.ConfigParser()
config.read('keys.ini')

# Now you can access the data stored in the INI file. For example, you can access the value of the 'hostname' key like this:
key = config['default']['key']

import os
import openai

openai.api_key = key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Human: Hello AI, how can we save our session to talk future? \nAI:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response)