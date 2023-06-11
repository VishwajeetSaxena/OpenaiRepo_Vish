import requests
import sseclient
import json

api_key = "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"
endpoint = "https://api.openai.com/v1/completions"

input = {
    "model": "text-davinci-003",
    "prompt": "Get me a tag line for birthday party",
    "max_tokens":30,
    "temperature": 0,
    "stream": True
}

#headers
headers = {
    'Accept': 'text/event-stream',
    'Authorization': 'Bearer ' + api_key
}

response = requests.post(endpoint, stream=True, headers=headers, json=input)
sseclient = sseclient.SSEClient(response)

for event in sseclient.events():
    if event.data != '[DONE]':
        print(json.loads(event.data)['choices'][0]['text'], end='', flush=True)