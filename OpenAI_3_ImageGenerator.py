from base64 import b64decode
import webbrowser
import openai


def generateImage_AndSave(prompt, image_count):
    images = []
    response = openai.Image.create(
        prompt = prompt,
        n= image_count,
        size = '512x512',
        response_format ='b64_json'
    )

    for image in response['data']:
        images.append(image.b64_json)

    prefix = 'Img'
    for index,image in enumerate(images):
        with open(f'{prefix}_{index}.jpg', 'wb') as file:
            file.write(b64decode(image))


openai.api_key = "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"

generateImage_AndSave('clouds',image_count=2)