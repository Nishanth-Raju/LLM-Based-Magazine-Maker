import requests
import ollama
from typing import cast, Dict, Any

class LLMHandler:
    def __init__(self, openrouter_api_key=None):
        self.openrouter_api_key = openrouter_api_key
        self.openrouter_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate_with_openrouter(self, prompt, model="microsoft/wizardlm-2-8x22b"):
        """Generate text using OpenRouter free API."""
        headers = {
            "Authorization": f"Bearer {self.openrouter_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
        response = requests.post(self.openrouter_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"OpenRouter API error: {response.status_code}")

    def generate_with_ollama(self, prompt, model="tinyllama"):
        """Generate text using Ollama locally."""
        try:
            response = ollama.generate(model=model, prompt=prompt)
            response_dict = cast(Dict[str, Any], response)
            return response_dict['response']
        except Exception as e:
            raise Exception(f"Ollama error: {e}")

    def generate(self, prompt):
        """Generate text with fallback and post-processing."""
        if self.openrouter_api_key:
            try:
                response = self.generate_with_openrouter(prompt)
            except:
                print("OpenRouter failed, falling back to Ollama.")
                response = self.generate_with_ollama(prompt)
        else:
            response = self.generate_with_ollama(prompt)
        return response

# Example usage
if __name__ == "__main__":
    llm = LLMHandler()
    print(llm.generate("Summarize this text: Hello world."))
