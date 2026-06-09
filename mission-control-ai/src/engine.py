import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src.alertas import *

load_dotenv()

TRILHA = "envirosat" 

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.2):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠ Erro ao consultar IA: {e}"

def load_system_prompt():
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de controle de missão espacial." 


class MissionEngine:

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

        self.alertas_atuais = alertas()
        
    def is_ready(self):
        return True



    def status_snapshot(self):
        
        return self.alertas_atuais 
        
        
    
    def analyze(self, pergunta_usuario):
       
        alertas_sistema = self.alertas_atuais
       
        
        prompt_final = (
            f"--- RELATÓRIO DE TELEMETRIA E ALERTAS DO SATÉLITE ---\n"
            f"{alertas_sistema}\n\n"
            f"--- PERGUNTA DO OPERADOR ---\n"
            f"{pergunta_usuario}")
        
        
       
        return llm(prompt_final, system=self.system_prompt)