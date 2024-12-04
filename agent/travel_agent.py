from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.output_parsers import OutputFixingParser
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool

def create_travel_agent(llm, tools):
    system_message = SystemMessage(
        content="""Você é um assistente de viagens sustentáveis.
        Seu objetivo é ajudar os usuários a planejar viagens ecológicas e de baixo impacto.
        Use as ferramentas disponíveis para fornecer informações precisas e úteis.
        Sempre inclua os resultados das ferramentas em sua resposta final."""
    )
    
    prompt = ChatPromptTemplate.from_messages([
        system_message,
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = OpenAIFunctionsAgent(llm=llm, prompt=prompt, tools=tools)
    
    # Adicione o OutputFixingParser
    output_parser = OutputFixingParser.from_llm(parser=agent.output_parser, llm=llm)
    agent.output_parser = output_parser

    executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )

    return executor, [tool.name for tool in tools], [tool.description for tool in tools]

def run_travel_agent(agent, tool_names, tool_strings, user_input):
    try:
        response = agent.run(input=user_input)
        return response
    except Exception as e:
        return f"Ocorreu um erro ao processar sua solicitação: {str(e)}\n\nPor favor, tente reformular sua pergunta."