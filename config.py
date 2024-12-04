import requests
from typing import List, Dict
from langchain.llms.base import LLM
from tools.destination_finder import sustainable_destinations_tool
from tools.carbon_calculator import carbon_footprint_tool
from tools.itinerary_optimizer import sustainable_itinerary_tool
from langchain_community.llms import OpenAI

from tools.tools import sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool

class LocalLLM(LLM):
    model: str
    temperature: float = 0.7

    def _call(self, prompt: str, stop: List[str] = None) -> str:
        url = "http://localhost:11434/api/chat"
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": self.temperature
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            content = response.json().get('message', {}).get('content', 'Sem resposta da LLM.')
            
            # Garantir que a resposta esteja no formato esperado
            if "Pensamento:" not in content and "Ação:" not in content and "Resposta Final:" not in content:
                content = f"Pensamento: {content}\nResposta Final: {content}"
            
            return content
        except requests.RequestException as e:
            return f"Erro na requisição: {str(e)}"

    @property
    def _llm_type(self) -> str:
        return "local_llm"

def get_local_models() -> List[str]:
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            data = response.json()
            return [model['name'] for model in data.get('models', [])]
        else:
            print(f"Erro ao obter modelos: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        return []

def setup_langchain(model: str, temperature: float = 0.7):
    llm = LocalLLM(model=model, temperature=temperature)
    tools = [
        sustainable_destinations_tool,
        carbon_footprint_tool,
        sustainable_itinerary_tool
    ]
    return llm, tools