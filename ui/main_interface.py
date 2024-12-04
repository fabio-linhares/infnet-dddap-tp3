import streamlit as st
from agent.travel_agent import run_travel_agent

def render_main_interface(agent, tool_names, tool_strings):
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_started" not in st.session_state:
        st.session_state.chat_started = False

    if not st.session_state.chat_started:
        st.title("Parte Prática")
        st.markdown("""
            <h3 style="color: #2E86C1;">Como funciona o Ecossistema Inteligente?</h3>
            <p style="text-align: justify; font-size: 16px; line-height: 1.6;">
            O sistema utiliza o framework LangChain, que integra ferramentas personalizadas com um raciocínio baseado no modelo ReAct (*Reasoning and Acting*). Isso permite que o agente execute ações inteligentes, como busca de informações, recomendações e resolução de problemas com base em dados fornecidos pelo usuário.
            </p>
            <h4>Principais Funcionalidades:</h4>
            <ul style="font-size: 16px;">
                <li>Memória conversacional para respostas mais contextuais e relevantes.</li>
                <li>Planejamento de viagens com base em critérios personalizados.</li>
                <li>Interface intuitiva e responsiva.</li>
            </ul>
            <p style="text-align: justify; font-size: 16px; line-height: 1.6;">
            Explore esta página para entender mais sobre o sistema e tirar dúvidas específicas sobre sua operação.
            </p>
            """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Descreva seus objetivos de viagem e quaisquer restrições:")
    if prompt:
        st.session_state.chat_started = True
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Criando seu plano de viagem sustentável personalizado..."):
                response = run_travel_agent(agent, tool_names, tool_strings, prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
