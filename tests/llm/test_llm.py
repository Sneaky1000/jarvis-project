from jarvis.llm.local_model import LocalModelLLM

if __name__ == "__main__":
    llm = LocalModelLLM()  # Will download model on first run if needed
    prompt = "How can I run LLMs efficiently on my laptop?"
    reply = llm.generate(prompt)
    print("LLM response:", reply)
