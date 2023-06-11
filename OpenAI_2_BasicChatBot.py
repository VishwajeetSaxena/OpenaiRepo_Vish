import os
import openai
import gradio as gr

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
prompt = "Please type your question here"



def openai_create(prompt):
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
    return response.choices[0].text

# def openai_create(prompt):
    
#     response = openai.Completion.create(
#         model = "text=davinci-003",
#         prompt = "Hi how are you",
#         max_tokens = 150,
#         temparature = 0.7,
#         top_p = 1,
#         stop = ["Human:", "AI:"],
#         presence_penalty = 0.6,
#         frequency_penalty = 0,
#     )
#     print(response)
#     return response.choices[0].text

def conversation_history(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input,output))
    return history, history

blocks = gr.Blocks()


with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Click")
    submit.click(conversation_history,inputs=[message,state], outputs=[chatbot,state])

blocks.launch(share=True)