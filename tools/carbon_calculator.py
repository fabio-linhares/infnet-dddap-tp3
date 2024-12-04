from langchain.agents import Tool
import random

def calculate_advanced_carbon_footprint(travel_details: str) -> str:
    transport_emissions = random.uniform(100, 1000)
    accommodation_emissions = random.uniform(50, 500)
    activity_emissions = random.uniform(20, 200)
    total_emissions = transport_emissions + accommodation_emissions + activity_emissions
    
    compensation_methods = [
        "Plantio de árvores",
        "Investimento em energia renovável",
        "Apoio a projetos de conservação"
    ]
    
    local_impact = [
        "Aumento do turismo sustentável",
        "Geração de empregos locais",
        "Preservação de áreas naturais"
    ]
    
    result = f"""
[CÁLCULO DE PEGADA DE CARBONO]
Detalhes da viagem: {travel_details}
Emissões de transporte: {transport_emissions:.2f} kg CO2
Emissões de acomodação: {accommodation_emissions:.2f} kg CO2
Emissões de atividades: {activity_emissions:.2f} kg CO2
Total de emissões: {total_emissions:.2f} kg CO2

Métodos de compensação recomendados:
- {random.choice(compensation_methods)}
- {random.choice(compensation_methods)}

Impacto na comunidade local:
- {random.choice(local_impact)}
- {random.choice(local_impact)}
[FIM DO CÁLCULO DE PEGADA DE CARBONO]
"""
    return result

carbon_footprint_tool = Tool(
    name="Cálculo Avançado de Pegada de Carbono e Impacto Local",
    func=calculate_advanced_carbon_footprint,
    description="Calcula a pegada de carbono detalhada da viagem, sugere métodos de compensação e avalia o impacto na comunidade local"
)