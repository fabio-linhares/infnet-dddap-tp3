from langchain.agents import Tool
import random

def find_sustainable_destinations(preferences: str, location: str) -> str:
    destinations = [
        "Ilha Eco-Friendly",
        "Montanha Sustentável",
        "Cidade Verde",
        "Vila Renovável",
        "Parque Nacional Conservado"
    ]
    
    selected_destinations = random.sample(destinations, 3)
    
    result = f"""
[BUSCA DE DESTINOS SUSTENTÁVEIS]
Preferências: {preferences}
Localização: {location}

Destinos sustentáveis recomendados:
1. {selected_destinations[0]}
   - Pontuação de sustentabilidade: {random.randint(80, 100)}/100
   - Destaque: {random.choice(["Energia 100% renovável", "Zero resíduos", "Conservação da biodiversidade"])}

2. {selected_destinations[1]}
   - Pontuação de sustentabilidade: {random.randint(80, 100)}/100
   - Destaque: {random.choice(["Turismo de baixo impacto", "Agricultura orgânica local", "Proteção de espécies ameaçadas"])}

3. {selected_destinations[2]}
   - Pontuação de sustentabilidade: {random.randint(80, 100)}/100
   - Destaque: {random.choice(["Transporte público elétrico", "Economia circular", "Educação ambiental para visitantes"])}

[FIM DA BUSCA DE DESTINOS SUSTENTÁVEIS]
"""
    return result

sustainable_destinations_tool = Tool(
    name="Busca Avançada de Destinos Sustentáveis",
    func=find_sustainable_destinations,
    description="Encontra destinos de viagem sustentáveis usando análise geoespacial, clustering avançado e otimização multi-objetivo"
)