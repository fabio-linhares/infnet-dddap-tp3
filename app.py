import streamlit as st
import os
from config import setup_langchain, get_local_models
from agent.travel_agent import create_travel_agent
from ui.main_interface import render_main_interface
from streamlit import session_state
from tools import sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool

from tools.tools import sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool
from langchain.llms import OpenAI  # ou qualquer outro modelo que você esteja usando
from langchain_community.llms import OpenAI 
from langchain_community.chat_models import ChatOpenAI 


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def render_explanations():
    st.title("Parte Teórica:")
    
    menu_items = [
        "1. Definição do Problema",
        "2. Configuração do Framework LangChain",
        "3. Implementação de Ferramentas",
        "4. Utilização do Framework ReAct",
        "5. Adição de Memória Conversacional",
        "6. Desenvolvimento da Lógica do Agente",
        "7. Projeto da Interface do Usuário",
        "8. Teste da Solução",
        "9. Documentação do Projeto",
        "10. Boas Práticas de Codificação"
    ]
    
    selected_item = st.selectbox("Selecione um tópico:", menu_items)
    
    file_mapping = {
        "1. Definição do Problema": "1_definicao_do_problema.txt",
        "2. Configuração do Framework LangChain": "2_configuracao_do_framework_langchain.txt",
        "3. Implementação de Ferramentas": "3_implementacao_de_ferramentas.txt",
        "4. Utilização do Framework ReAct": "4_utilizacao_do_framework_react.txt",
        "5. Adição de Memória Conversacional": "5_adicao_de_memoria_conversacional.txt",
        "6. Desenvolvimento da Lógica do Agente": "6_desenvolvimento_da_logica_do_agente.txt",
        "7. Projeto da Interface do Usuário": "7_projeto_da_interface_do_usuario.txt",
        "8. Teste da Solução": "8_teste_da_solucao.txt",
        "9. Documentação do Projeto": "9_documentacao_do_projeto.txt",
        "10. Boas Práticas de Codificação": "10_boas_praticas_de_codificacao.txt"
    }
    
    file_name = file_mapping.get(selected_item)
    if file_name:
        file_path = os.path.join('data', file_name)
        if os.path.exists(file_path):
            content = read_file_content(file_path)
            st.markdown(content)
        else:
            st.error(f"Arquivo não encontrado: {file_path}")
    else:
        st.error("Seleção inválida")

def render_main_page():
    st.title("Desenvolvimento de Data-Driven Apps com Python")
    
    with open('data/apresentacao.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    st.markdown(content, unsafe_allow_html=True)

def render_explanations_page(agent, tool_names, tool_strings):
    render_main_interface(agent, tool_names, tool_strings)
        
def render_footer():
    st.markdown("""
        <style>
        .footer {
            position: relative;
            bottom: 0;
            width: 100%;
            color: #F8F8F8;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            margin-top: 20px;
        }
        .footer a {
            color: #F4D03F;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            <p>Professor: Fernando Guimarães | Aluno: Fábio Linhares</p>
            <p>Instituto: Instituto Infnet | Ciência de Dados</p>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="Ecossistema de Viagens Sustentáveis")
    
    with st.sidebar:
        st.image("images/infnetlogo.png", use_container_width=True)
        st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
        st.image("images/infnet30anos.png", use_container_width=True)
        
        st.markdown("<h2 style='color: #2E86C1;'>Configurações</h2>", unsafe_allow_html=True)
        models = get_local_models()
        selected_model = st.selectbox("Selecione o modelo:", models)
        temperature = st.slider("Temperatura", 0.1, 1.0, 0.7, 0.1)
        st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
        
        page = st.selectbox("Selecione a página:", ["Apresentação", "Parte Teórica", "Parte Prática"])

    tools = [sustainable_destinations_tool, carbon_footprint_tool, sustainable_itinerary_tool]
    llm, _ = setup_langchain(selected_model, temperature)
    agent, tool_names, tool_strings = create_travel_agent(llm, tools)


    if page == "Apresentação":
        render_main_page()
    elif page == "Parte Teórica":
        render_explanations()
    elif page == "Parte Prática":
        render_explanations_page(agent, tool_names, tool_strings)


    render_footer()

if __name__ == "__main__":
    main()

