from langchain.agents import Tool

import random
import json

def find_sustainable_destinations(preferences: str, location: str = "") -> str:
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

def calculate_carbon_footprint(travel_details: str) -> str:
    transport_emissions = random.uniform(100, 1000)
    accommodation_emissions = random.uniform(50, 500)
    activity_emissions = random.uniform(20, 200)
    total_emissions = transport_emissions + accommodation_emissions + activity_emissions
    
    result = f"""
[CÁLCULO DE PEGADA DE CARBONO]
Detalhes da viagem: {travel_details}
Emissões de transporte: {transport_emissions:.2f} kg CO2
Emissões de acomodação: {accommodation_emissions:.2f} kg CO2
Emissões de atividades: {activity_emissions:.2f} kg CO2
Total de emissões: {total_emissions:.2f} kg CO2

Métodos de compensação recomendados:
- {random.choice(["Plantio de árvores", "Investimento em energia renovável", "Apoio a projetos de conservação"])}
- {random.choice(["Plantio de árvores", "Investimento em energia renovável", "Apoio a projetos de conservação"])}

[FIM DO CÁLCULO DE PEGADA DE CARBONO]
"""
    return result

def optimize_sustainable_itinerary(preferences: str, constraints: str = "") -> str:
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

sustainable_destinations_tool = Tool(
    name="Busca Avançada de Destinos Sustentáveis",
    func=find_sustainable_destinations,
    description="Encontra destinos de viagem sustentáveis baseado nas preferências do usuário"
)

carbon_footprint_tool = Tool(
    name="Cálculo Avançado de Pegada de Carbono",
    func=calculate_carbon_footprint,
    description="Calcula a pegada de carbono detalhada da viagem"
)

sustainable_itinerary_tool = Tool(
    name="Otimização de Itinerário Sustentável",
    func=optimize_sustainable_itinerary,
    description="Cria um itinerário de viagem otimizado para sustentabilidade"
)

# from langchain.agents import Tool
# import json

# def find_sustainable_destinations(query: str) -> str:
#     # Simulação de busca de destinos sustentáveis
#     destinations = [
#         {"name": "Ilha Eco", "description": "Uma ilha com foco em ecoturismo"},
#         {"name": "Montanha Verde", "description": "Destino de montanha com práticas sustentáveis"},
#         {"name": "Cidade Sustentável", "description": "Uma cidade urbana com iniciativas verdes"}
#     ]
#     return json.dumps(destinations)

# def calculate_carbon_footprint(travel_details: str) -> str:
#     # Simulação de cálculo de pegada de carbono
#     return "A pegada de carbono estimada para esta viagem é de 500kg de CO2."

# def optimize_sustainable_itinerary(preferences: str) -> str:
#     # Simulação de otimização de itinerário
#     return "Itinerário otimizado: Dia 1 - Passeio de bicicleta, Dia 2 - Visita a fazenda orgânica, Dia 3 - Trilha ecológica"

# sustainable_destinations_tool = Tool(
#     name="Busca Avançada de Destinos Sustentáveis",
#     func=find_sustainable_destinations,
#     description="Encontra destinos de viagem sustentáveis baseado nas preferências do usuário"
# )

# carbon_footprint_tool = Tool(
#     name="Cálculo Avançado de Pegada de Carbono",
#     func=calculate_carbon_footprint,
#     description="Calcula a pegada de carbono detalhada da viagem"
# )

# sustainable_itinerary_tool = Tool(
#     name="Otimização de Itinerário Sustentável",
#     func=optimize_sustainable_itinerary,
#     description="Cria um itinerário de viagem otimizado para sustentabilidade"
#)