# Germinare - FastAPI App

Este é um projeto de exemplo usando **FastAPI** para desenvolver uma API com conexão a um banco de dados PostgreSQL.

## Pré-requisitos

Antes de rodar o projeto, verifique se você tem os seguintes requisitos instalados:

- **Python 3.12+**
- **PostgreSQL**
- **Pip** (gerenciador de pacotes do Python)

## Instalação

Siga os passos abaixo para configurar o ambiente e rodar o aplicativo.

### 1. Clone o repositório

Clone o repositório para o seu ambiente local:

### 2. Crie um ambiente virtual
Crie um ambiente virtual para o seu projeto:

python3 -m venv venv
Ative o ambiente virtual:

No Linux/macOS:

source venv/bin/activate
No Windows:

venv\Scripts\activate
### 3. Instale as dependências
Instale as dependências necessárias usando o pip:

pip install -r requirements.txt
### 4. Configure o banco de dados
Certifique-se de que o PostgreSQL está instalado e configurado corretamente.

Crie um banco de dados no PostgreSQL. Acesse o PostgreSQL e execute o comando:

CREATE DATABASE seu_banco;
Crie um usuário no PostgreSQL (se ainda não existir) e garanta que ele tenha permissões adequadas para criar tabelas:

Para popular o banco pode usar: 
INSERT INTO soybean_meal_prices (id, contract_month, price, created_at)
VALUES                  
  ('uuid-gerado-1', '2023-01', 350.50, CURRENT_TIMESTAMP),
  ('uuid-gerado-2', '2023-02', 360.75, CURRENT_TIMESTAMP),
  ('uuid-gerado-3', '2023-03', 370.25, CURRENT_TIMESTAMP);


### 5. Inicie o servidor
Agora, você pode iniciar o servidor de desenvolvimento do FastAPI:

uvicorn app.main:app --reload
O servidor será iniciado no endereço http://127.0.0.1:8000. Você pode acessar a documentação automática da API em:

Swagger UI: http://127.0.0.1:8000/docs



### 6. CURL
curl --location 'http://127.0.0.1:8000/api/flat_price' \
--header 'Content-Type: application/json' \
--data '{
  "basis": 100.0,
  "contract_months": ["2023-01", "2023-02", "2023-03"]
}'
