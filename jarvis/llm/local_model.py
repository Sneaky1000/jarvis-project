from gpt4all import GPT4All

class LocalModelLLM:
    def __init__(self, model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf"):
        """
        GPT4All automatically downloads the specified model if not found locally.
        """
        self.model = GPT4All(model_name)

    def generate(self, prompt, max_tokens=100):
        """
        Generate text from the local LLM based on a prompt.
        """
        response = self.model.generate(
            prompt,
            max_tokens=max_tokens,
            # You can set other parameters like temperature=0.7, top_k=40, etc.
        )
        return response
