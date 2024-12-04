from langchain.memory import ConversationEntityMemory
from config import CONVERSATION_MEMORY_K

class ConversationMemory(ConversationEntityMemory):
    def __init__(self, llm):
        super().__init__(llm=llm, k=CONVERSATION_MEMORY_K)

    # Adicione métodos personalizados conforme necessário