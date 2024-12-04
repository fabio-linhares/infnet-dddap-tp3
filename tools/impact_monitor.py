from langchain.tools import Tool

def find_sustainable_destinations(query: str) -> str:
    return f"Destinos sustentáveis para: {query}"

sustainable_destinations_tool = Tool(
    name="Busca de Destinos Sustentáveis",
    func=find_sustainable_destinations,
    description="Encontra destinos de viagem sustentáveis"
)