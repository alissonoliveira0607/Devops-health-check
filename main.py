from flask import Flask, jsonify, request
import time
import requests
import os
import json
from dotenv import load_dotenv
import logging

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    handlers=[
                        logging.FileHandler('access.log'),
                        logging.StreamHandler()
                    ])

# Utilizar as variáveis de ambiente para as configurações
API_URL = os.getenv('API_URL')
API_AUTH_TOKEN = os.getenv('API_AUTH_TOKEN')

def check_api_health(headers, payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        return response.status_code == 200

    except Exception as e:
        logging.error(f"Erro na verificação da API: {e}")
        return False

def perform_health_check(headers, payload):
    api_health = check_api_health(headers, payload)
    # Adicione outras verificações aqui, se necessário

    return api_health

@app.route('/health', methods=['GET'])
def health_check():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_AUTH_TOKEN
    }
    
    with open('body.json', 'r') as body_file:
        payload = json.load(body_file)

    if perform_health_check(headers, payload):
        response = {
            "status": "ok",
            "message": "Todos os componentes estão saudáveis."
        }
        status_code = 200
    else:
        response = {
            "status": "erro",
            "message": "Alguns componentes estão com problemas."
        }
        status_code = 500

    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0')