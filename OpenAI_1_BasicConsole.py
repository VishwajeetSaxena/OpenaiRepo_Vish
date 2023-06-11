import os
import openai

openai.api_key = "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"

prompt = "Please tell name of 3 baby boy"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)