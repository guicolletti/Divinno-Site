from flask import Flask, render_template, request  # Corrigir a importação
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Configurar a API uma única vez
genai.configure(api_key=os.getenv('API'))
model = genai.GenerativeModel('gemini-1.0-pro-latest')

app = Flask(__name__)


@app.route('/search')
def search():
    context = ('Você é um bot de vinhos diversos a serviço da empresa Divinno, seu nome é Divinnobot, sua'
               'únia e exclusiva função é fazer com que os clientes descubram qual o melhor tipo de vinho'
               'para as mais demasiadas ocasiões. Apenas responda questões relacionadas à Divinno e sobre'
               'os tipos de vinhos oferecidos.')

    prompt = request.args.get('prompt')
    if not prompt:
        return {'message': 'Desculpe, não consegui entender sua pergunta. Pode tentar novamente?'}

    input_ia = f'{context}: {prompt}'
    try:
        output = model.generate_content(input_ia)
        return {'message': output.text}  # Retorna a resposta do modelo
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return {'message': 'Desculpe, houve um erro ao processar sua solicitação.'}

@app.route("/")
def inicial():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == '__main__':
    app.run(debug=True)