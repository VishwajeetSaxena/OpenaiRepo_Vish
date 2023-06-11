from base64 import b64decode
import webbrowser
import openai




def generateImage_AndOpen(prompt, image_count):
    images = []
    response = openai.Image.create(
        prompt = prompt,
        n = image_count,
        size = '512x512',
        response_format ='url'
    )

    for image in response['data']:
        webbrowser.open(image.url)



openai.api_key = "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"

generateImage_AndOpen('dog',image_count=2)