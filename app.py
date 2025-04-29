# import requests 
# import json
# import gradio as gr

# url="http://localhost:11434/api/generate"

# headers={
#     'Content-Type': 'application/json',
# }

# history = []
# def generate_response(prompt):
#     history.append(prompt)
#     final_propmt = "\n".join(history)
#     data={
#         "model":"CodeMitra",
#         "prompt":final_propmt,
#         "stream":False,
#     }

#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     if response.status_code == 200:
#         response=response.text
#         data=json.loads(response)
#         actual_response=data['response']
#         return actual_response
    
#     else:
#         print("Error:", response.status_code, response.text)

# interface = gr.Interface(
#     fn=generate_response,
#     inputs=gr.Textbox(lines=7, label="Enter your query"),
#     outputs=gr.Textbox(), 
#     title="CodeMitra",
# )
# interface.launch()



import aiohttp
import asyncio
import json
import gradio as gr

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}

history = []

async def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "CodeMitra",
        "prompt": final_prompt,
        "stream": False,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                response_data = await response.json()
                return response_data['response']
            else:
                return f"Error: {response.status}"

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=7, label="Enter your query"),
    outputs=gr.Textbox(), 
    title="CodeMitra",
)

interface.launch()
