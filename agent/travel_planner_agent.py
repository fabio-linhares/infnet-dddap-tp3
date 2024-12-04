from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import LLMChain
from tools.tools.carbon_footprint_calculator import CarbonFootprintCalculator
from tools.tools.local_experience_recommender import LocalExperienceRecommender
from tools.tools.impact_monitor import ImpactMonitor
from memory.conversation_memory import ConversationMemory

class TravelPlannerAgent:
    def __init__(self, llm):
        self.llm = llm
        self.memory = ConversationMemory(llm=self.llm)
        self.tools = [
            Tool(name="Carbon Footprint Calculator", func=CarbonFootprintCalculator().calculate),
            Tool(name="Local Experience Recommender", func=LocalExperienceRecommender().recommend),
            Tool(name="Impact Monitor", func=ImpactMonitor().monitor)
        ]
        
        self.prompt = self._create_prompt()
        self.llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)
        self.agent = LLMSingleActionAgent(
            llm_chain=self.llm_chain,
            output_parser=self._custom_output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent, tools=self.tools, verbose=True, memory=self.memory
        )

    def _create_prompt(self):
        # Implemente a lógica do prompt aqui
        pass

    def _custom_output_parser(self, llm_output):
        # Implemente o parser de saída personalizado aqui
        pass

    def plan_trip(self, user_input):
        return self.agent_executor.run(user_input)