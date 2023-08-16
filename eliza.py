import streamlit as st
import openai

# Configure the OpenAI API Key 
openai.api_key = "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"

def generate_chat_response(user_input):
    response = openai.Completion.create(
        engine="davinci-codex",  # Use the davinci-codex engine
        prompt=user_input,
        max_tokens=50  # You can adjust this value based on the desired response length
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chatbot de Atendimento Eliza")
    st.markdown("Bem-vindo ao nosso chatbot de atendimento psicológico com nossa querida Eliza. Sinta-se à vontade para conversar sobre seus sentimentos e preocupações.")

    user_input = st.text_area("Digite sua mensagem aqui:")

    if user_input:
        if st.button("Enviar"):
            bot_response = generate_chat_response(user_input)
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
        bot_response = generate_chat_response(selected_example)
        st.text("Resposta:")
        st.success(bot_response)

    st.write("Desenvolvido com ❤️ por [Denise Lins.. ]")

if __name__ == "__main__":
    main()
