import requests
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any

class OllamaLLM(LLM):
    model_name: str
    temperature: float = 0.7
    base_url: str = "http://localhost:11434/api"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        url = f"{self.base_url}/chat"
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": self.temperature
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get('message', {}).get('content', 'Sem resposta da LLM.')

    @property
    def _llm_type(self) -> str:
        return "ollama"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model_name": self.model_name, "temperature": self.temperature}