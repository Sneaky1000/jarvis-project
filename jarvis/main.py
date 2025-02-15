import sys
import os
from jarvis.audio.listener import AudioListener
from jarvis.llm.local_model import LocalModelLLM
from jarvis.audio.tts import say
from dotenv import load_dotenv

load_dotenv()

def main():
    username = os.getenv('USER_NAME')
    listener = AudioListener()
    llm = LocalModelLLM()

    print("Jarvis is running... Say something! (say 'Jarvis exit' to quit)")

    while True:
        command = listener.listen()

        if command is None:
            continue

        if command.lower() == "jarvis exit":
            print(f"Goodbye, {username}!")
            sys.exit(0)

        # Pass transcribed text to LLM
        prompt = f"You are a helpful assistant named Jarvis. The user said: {command}\nRespond to the user directly. Do not provide me any other information."
        response = llm.generate(prompt)
        print("LLM response:", response)
        say(response)

if __name__ == "__main__":
    main()
