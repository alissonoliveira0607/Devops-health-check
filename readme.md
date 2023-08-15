# Aplicação de Health Check

Esta é uma aplicação de health check simples que verifica a disponibilidade de endpoints de diferentes APIs. Ela utiliza o framework Flask para criar um servidor web e a biblioteca `requests` para fazer as verificações.

## Pré-requisitos

- Python 3.8 ou superior instalado
- Gerenciador de pacotes `pip` instalado
- Docker (opcional, para executar a aplicação em um contêiner)

## Configuração

1. Clone o repositório:

```shell
git clone https://github.com/seu-usuario/seu-repositorio.git
```

## Acesse o diretório da aplicação
```shell
cd seu-repositorio
```

## Instale as dependências:
```python
pip install -r requirements.txt
```

## Variáveis de Ambiente:
Crie um arquivo .env no mesmo diretório do arquivo main.py com as seguintes variáveis de ambiente:
- API_URL=endpoint
- API_AUTH_TOKEN=Bearer seu_token
Substitua os valores de API_URL e API_AUTH_TOKEN pelas informações apropriadas da sua configuração.

Configurações de Headers e body
Os headers da requisição e o corpo da requisição são definidos nos arquivos headers.json e body.json, respectivamente. Certifique-se de que esses arquivos estejam no mesmo diretório que o arquivo main.py.

Arquivo headers.json:

```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer $API_AUTH_TOKEN"
}
```

Arquivo body.json:
```json
{
    "consulta": [{
        "pedido": "00001"
    }]
}
```

Executando a Aplicação
Você pode executar a aplicação diretamente no seu ambiente local ou em um contêiner Docker.

Localmente:
python main.py


Com Docker
Construa a imagem Docker:
No diretório que encontra-se o Dockerfile execute o seguinte comando
- docker build -t health-check-app .


Execute o contêiner:
- docker run -p 5000:5000 --env-file .env health-check-app


Acesse a aplicação no navegador em http://localhost:5000/health.

