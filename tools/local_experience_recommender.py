from langchain.agents import Tool
import random

def recommend_local_experiences(location: str) -> str:
    experiences = [
        "Aula de culinária tradicional",
        "Tour de arte de rua",
        "Oficina de artesanato local",
        "Visita a mercado de produtores",
        "Apresentação de música folclórica",
        "Passeio histórico guiado por morador",
        "Experiência de pesca sustentável"
    ]
    
    selected_experiences = random.sample(experiences, 3)
    
    result = f"""
[RECOMENDAÇÃO DE EXPERIÊNCIAS LOCAIS]
Local: {location}

Experiências locais sustentáveis recomendadas:
1. {selected_experiences[0]}
   - Autenticidade: {random.randint(80, 100)}%
   - Impacto na comunidade: Muito positivo

2. {selected_experiences[1]}
   - Autenticidade: {random.randint(80, 100)}%
   - Impacto na comunidade: Positivo

3. {selected_experiences[2]}
   - Autenticidade: {random.randint(80, 100)}%
   - Impacto na comunidade: Muito positivo

Todas as experiências são operadas por membros da comunidade local e seguem práticas sustentáveis.
[FIM DA RECOMENDAÇÃO DE EXPERIÊNCIAS LOCAIS]
"""
    return result

local_experience_tool = Tool(
    name="Recomendador de Experiências Locais Sustentáveis",
    func=recommend_local_experiences,
    description="Recomenda experiências locais autênticas e sustentáveis"
)