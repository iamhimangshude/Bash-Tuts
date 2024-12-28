import os
import re
import google.generativeai as genai # pip install google-generativeai
import time

# setup virtual environment before running this script!
"""Usage:
1. Create a virtual environment (python -m venv .venv) and activate it (source .vnv/bin/activate)
2. pip install -r requirements.txt
3. python py-ai.py

For automation, you can set alias in the customBashPrompt.sh file!
"""

API_KEY = os.environ.get("GENAI_API_KEY", "Not Found")


def strip_markdown(text):
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def chat_api_call(prompt: str = "Hello", history:list = []) -> list:
    """
    Calls the Google Generative AI API to get a response
    
    `returns` the history as list
    """
    
    if prompt == "":
        prompt = "Hello"
    
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 2048,
        },
    )
    
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(prompt)
    strippedText = strip_markdown(response.text)
    history.append({"role": "user", "parts": [prompt + "\n"]})
    history.append({"role": "model", "parts": [strippedText + "\n"]})
    for text in strippedText:
        print(text, end="", flush=True)
        time.sleep(0.01)
    return history


if __name__ == "__main__":
    chat_history:list = None
    print("Ask to AI")
    while True:
        try:
            userPrompt:str = input("You: ")
            print("AI:\n")
            chat_history:list = chat_api_call(userPrompt, chat_history or [])
            print()
        except KeyboardInterrupt:
            print()
            break
