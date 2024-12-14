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

API_KEY = os.environ.get('GENAI_API_KEY', 'Not Found')

def strip_markdown(text):
    return re.sub(r'\*\*(.*?)\*\*', r'\1', text).strip()


def chat_api_call(prompt: str = 'Draft a baby rhyme!'):
    """Calls the Google Generative AI API to get a response"""
    if prompt == '':
        prompt = 'Draft a baby rhyme!'
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    strippedText = strip_markdown(response.text)
    for text in strippedText:
        print(text, end='', flush=True)
        time.sleep(0.01)
    


if __name__ == "__main__":
    print("ASK to AI")
    while True:
        try:
            userPrompt = input("You: ")
            print("AI:\n")
            chat_api_call(userPrompt)
            print()
        except KeyboardInterrupt:
            print()
            break

