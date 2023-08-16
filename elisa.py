from flask import Flask, render_template
import gradio
import openai as gpt

app = Flask (__name__)

# Configure a API Key do OpenAI (substitua pela sua chave)
gpt.api_key = "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"

def chatbot_interface(Converse_comigo):
    completion = gpt.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": Converse_comigo}])
    return completion.choices[0].message["content"]

inputs = gradio.Interface(
    fn=chatbot_interface,
    inputs="textbox",
    outputs="text",
    title="Chatbot de Atendimento Eliza",
    description="Bem-vindo ao nosso chatbot de atendimento psicológico com nossa querida Eliza. Sinta-se à vontade para conversar sobre seus sentimentos e preocupações.",
    examples=[
        ["Oi, estou me sentindo um pouco sobrecarregado hoje."],
        ["Como posso lidar com o estresse do trabalho?"],
        ["Gostaria de aprender a relaxar."]
    ]
)

@app.route("/")
def homepage():
    return render_template("homepage.html")

# Iniciar interface Gradio no endpoint "/chat"
inputs.launch(share=True, debug=True)

if _name_ == "_main_":
    app.run(debug=True)
