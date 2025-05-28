import os
import re
import google.generativeai as genai  # pip install google-generativeai
import time

# setup virtual environment before running this script!
"""Usage:
1. Create a virtual environment (python -m venv .venv) and activate it (source .vnv/bin/activate)
2. pip install -r requirements.txt
3. python py-ai.py

For automation, you can set alias in the customBashPrompt.sh file!
"""

API_KEY = os.environ.get("GENAI_API_KEY", "Not Found")
if API_KEY == "Not Found":
    print("Please set API KEY environment variable")
    exit()

genai.configure(api_key=API_KEY)
MODEL = "gemma-3-1b-it"


def strip_markdown(text):
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def chat_api_call(prompt: str = "Hello", history: list = [], config: dict = {}) -> list:
    """
    Calls the Google Generative AI API to get a response

    `returns` the history as list
    """

    if prompt == "":
        prompt = "Hello"

    if config == {} or config == None:
        config = {
            "temperature": 2,
            "max_output_tokens": 1024,
        }

    model = genai.GenerativeModel(
        model_name=MODEL,
        generation_config=config,
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
    chat_history: list = list()
    ai_config = {
        "temperature": 0.5,
        "max_output_tokens": 2048,
    }
    print("Ask to AI / Ctrl+C for options\n")
    while True:
        try:
            userPrompt: str = input("You: ")
            print()
            print("AI:\n")
            chat_history: list = chat_api_call(
                userPrompt, chat_history or [], ai_config
            )
            print()
        except KeyboardInterrupt:
            print()
            print(
                "Options:\n1. Change temperature/creativity\n2. Change max output tokens\n3. Change model\n4. Get chat history\n9. Back\n0. Exit"
            )
            choice = int(input("Choice: "))
            match choice:
                case 1:
                    temperature = float(input("Enter temperature (0-2): "))
                    ai_config["temperature"] = temperature
                    print("Current Configuration: ", ai_config)
                    print()

                case 2:
                    max_output_tokens = int(input("Enter max output tokens: "))
                    ai_config["max_output_tokens"] = max_output_tokens
                    print("Current Configuration: ", ai_config)
                    print()

                case 3:
                    print(f"Was using {MODEL}...")
                    print("Fetching list...")
                    model_list = [
                        model.name.strip("models/") for model in genai.list_models()
                    ]
                    print("Available Models:")
                    for i, model in enumerate(model_list):
                        print(f"{i}. {model}")
                    model_choice = int(input("Enter model choice: "))
                    MODEL = model_list[model_choice]
                    print("Using Model: ", MODEL)
                    print()

                case 4:
                    with open("genai-chat-history.txt", "a") as histFile:
                        histFile.write(str(chat_history))
                    print()

                case 0:
                    break

                case 9:
                    continue

                case _:
                    print("Invalid choice")
                    continue
