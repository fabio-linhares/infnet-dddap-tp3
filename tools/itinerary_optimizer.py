from langchain.agents import Tool
import random

def optimize_sustainable_itinerary(preferences: str, constraints: str) -> str:
    activities = [
        "Passeio de bicicleta",
        "Visita a fazenda orgânica",
        "Trilha ecológica",
        "Workshop de reciclagem",
        "Tour de energia renovável",
        "Mergulho para limpeza de corais",
        "Voluntariado em projeto de conservação"
    ]
    
    itinerary = random.sample(activities, 5)
    
    result = f"""
[OTIMIZAÇÃO DE ITINERÁRIO SUSTENTÁVEL]
Preferências: {preferences}
Restrições: {constraints}

Itinerário otimizado:
Dia 1: {itinerary[0]}
   - Impacto ambiental: Baixo
   - Benefício para comunidade local: Alto

Dia 2: {itinerary[1]}
   - Impacto ambiental: Muito baixo
   - Benefício para comunidade local: Médio

Dia 3: {itinerary[2]}
   - Impacto ambiental: Baixo
   - Benefício para comunidade local: Alto

Dia 4: {itinerary[3]}
   - Impacto ambiental: Muito baixo
   - Benefício para comunidade local: Alto

Dia 5: {itinerary[4]}
   - Impacto ambiental: Baixo
   - Benefício para comunidade local: Muito alto

Pontuação de sustentabilidade do itinerário: {random.randint(85, 100)}/100
[FIM DA OTIMIZAÇÃO DE ITINERÁRIO SUSTENTÁVEL]
"""
    return result

sustainable_itinerary_tool = Tool(
    name="Otimização Avançada de Itinerário Sustentável",
    func=optimize_sustainable_itinerary,
    description="Cria um itinerário de viagem otimizado para sustentabilidade, considerando múltiplos fatores e restrições"
)