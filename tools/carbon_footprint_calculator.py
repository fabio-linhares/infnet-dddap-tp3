from langchain.tools import Tool

def calculate_carbon_footprint(travel_details: str) -> str:
    return f"Pegada de carbono para: {travel_details}"

carbon_footprint_tool = Tool(
    name="Calculadora de Pegada de Carbono",
    func=calculate_carbon_footprint,
    description="Calcula a pegada de carbono da viagem"
)