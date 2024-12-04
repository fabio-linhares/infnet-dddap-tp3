from langchain_community.chat_models import ChatOpenAI
from agent.travel_agent import create_travel_agent, run_travel_agent
from tools import sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool

def test_agents():
    print("Testando as ferramentas do agente de viagens sustentáveis:")

    print("\n1. Testando a Busca Avançada de Destinos Sustentáveis:")
    destinos = sustainable_destinations_tool.func("Praias limpas e ecoturismo", "América do Sul")
    print(destinos)

    print("\n2. Testando o Cálculo Avançado de Pegada de Carbono:")
    pegada = carbon_footprint_tool.func("Voo de São Paulo para Florianópolis, hospedagem em hotel por 5 dias, passeios locais")
    print(pegada)

    print("\n3. Testando a Otimização de Itinerário Sustentável:")
    itinerario = sustainable_itinerary_tool.func("Atividades ao ar livre e experiências culturais", "Orçamento limitado")
    print(itinerario)

    print("\nTestando o agente completo:")
    tools = [sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool]
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
    agent, tool_names, tool_strings = create_travel_agent(llm, tools)

    user_input = "Quero planejar uma viagem sustentável para o Brasil. Pode me ajudar a encontrar destinos, calcular a pegada de carbono e criar um itinerário?"
    response = run_travel_agent(agent, tool_names, tool_strings, user_input)
    print(f"\nResposta do agente:\n{response}")

if __name__ == "__main__":
    test_agents()