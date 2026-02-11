# 🤖 Assistente Financeiro com IA - Projeto QA

Este projeto consiste em uma API de um assistente financeiro inteligente, desenvolvida para demonstrar fundamentos de Garantia de Qualidade (QA) e Automação de Testes.

## 🚀 Tecnologias Utilizadas
* **Backend:** Python com FastAPI
* **Testes de API:** Postman
* **Servidor:** Uvicorn

## 🧪 Testes Realizados
Atualmente, o projeto conta com validações automatizadas no Postman para:
1. Verificação de Status Code (200 OK).
2. Validação da lógica de categorias (Investimentos/Suporte).
3. Integridade do contrato da resposta (JSON).

## 🛠️ Como rodar o projeto
1. Instale as dependências: `pip install fastapi uvicorn`
2. Inicie o servidor: `python -m uvicorn main:app --reload`