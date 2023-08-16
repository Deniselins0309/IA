import streamlit as st
import openai as gpt

# Configure the OpenAI API Key (replace with your own key)
gpt.api_key = "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"

def chatbot_interface(Converse_comigo):
    completion = gpt.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": Converse_comigo}])
    return completion.choices[0].message["content"]

st.title("Chatbot de Atendimento Eliza")
st.markdown("Bem-vindo ao nosso chatbot de atendimento psicológico com nossa querida Eliza. Sinta-se à vontade para conversar sobre seus sentimentos e preocupações.")

user_input = st.text_area("Digite sua mensagem aqui:")

if user_input:
    bot_response = chatbot_interface(user_input)
    st.text("Resposta:")
    st.success(bot_response)

st.sidebar.title("Exemplos:")
st.sidebar.write("Selecione um exemplo para iniciar a conversa:")
examples = [
    "Oi, estou me sentindo um pouco sobrecarregado hoje.",
    "Como posso lidar com o estresse do trabalho?",
    "Gostaria de aprender a relaxar."
]
selected_example = st.sidebar.selectbox("Exemplos:", examples)

if st.sidebar.button("Iniciar Conversa"):
    bot_response = chatbot_interface(selected_example)
    st.text("Resposta:")
    st.success(bot_response)

st.write("Desenvolvido com ❤️ por [Denise Lins]")
