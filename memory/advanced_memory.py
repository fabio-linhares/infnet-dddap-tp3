import json

class AdvancedTravelMemorySystem:
    def __init__(self, llm):
        self.llm = llm
        self.chat_memory = []

    def add_to_memory(self, human_input, ai_output):
        self.chat_memory.append({"role": "user", "message": human_input})
        self.chat_memory.append({"role": "assistant", "message": ai_output})

    def query_memory(self, query):
        # Implemente a lógica de consulta à memória conforme necessário
        pass

    def generate_insights(self):
        # Implemente a lógica para gerar insights conforme necessário
        pass

    def save_memory(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_memory, f)

    def load_memory(self, filename):
        with open(filename, 'r') as f:
            self.chat_memory = json.load(f)