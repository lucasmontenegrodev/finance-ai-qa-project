from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Criando um modelo para a pergunta do usuário
class Pergunta(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"status": "IA Financeira Ativa", "usuario": "Lucas"}

@app.post("/chat")
def responder_chat(pergunta: Pergunta):
    texto_usuario = pergunta.texto.lower()
    
    # Simulação de lógica de IA Financeira
    if "rendimento" in texto_usuario:
        return {
            "resposta": "O rendimento médio do CDB hoje é de 100% do CDI.",
            "categoria": "investimentos"
        }
    elif "ajuda" in texto_usuario:
        return {
            "resposta": "Posso te ajudar com dúvidas sobre CDB, Poupança e Gastos.",
            "categoria": "suporte"
        }
    else:
        return {
            "resposta": "Desculpe, ainda estou aprendendo sobre esse assunto financeiro.",
            "categoria": "desconhecido"
        }