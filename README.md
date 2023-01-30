## Configuração e Inicialização da Aplicação

### 1. Clone o repositório da aplicação usando o comando abaixo:

- `git clone `

### 2. Na raiz do projeto, utilize o seguinte comando para adicionar os arquivos necessários para o uso do ambiente virtual:

- `python -m venv myvenv`

### 3. Inicialize o ambiente virtual com o seguinte comando:

#### Windowns

- `myvenv/Scripts/activate`

#### Linux/macOS

- `myvenv/bin/activate`

### 4. Instale as dependências do projeto com o seguinte comando:

- `pip install -r requirements.txt`

### 5. Execute as migrations para a configuração do banco de dados através dos seguintes comandos:

- `python manage.py makemigrations`
- `python manage.py migrate`

## Tecnologias ultilizadas:

- Python3
- Django
- Django Rest Framework
- Sqlite3

## API CNAB

### Introdução

Essa aplicação foi desenvolvida com o propósito de fornecer um API capaz de receber um arquivo .txt e fazer com que os dados passados no mesmo fossem parseados e armazenados em um banco de dados.

### Rotas

#### URL -> http://127.0.0.1:8000/

#### `POST api/file/ - FORMATO DE REQUISIÇÃO`

```json
CNAB.txt
```

#### `POST api/file/ - FORMATO DE RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "file": "http://127.0.0.1:8000/data_file/CNAB.txt"
}
```

#### `GET api/companies/ - FORMATO DE REQUISIÇÃO`

```json
Vazio
```

#### `GET api/companies/ - FORMATO DE RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "transactions": [
      {
        "id": 1,
        "type": 3,
        "date": "2019-03-01",
        "value": 142.0,
        "CPF": "09620676017",
        "card": "4753****3153",
        "hour": "2019-03-01T05:34:53Z",
        "company": 1
      }
    ],
    "account_balance": -204.0,
    "store_owner": "JOÃO MACEDO",
    "store_name": "BAR DO JOÃO"
  },
  {
    "id": 2,
    "transactions": [
      {
        "id": 2,
        "type": 5,
        "date": "2019-03-01",
        "value": 132.0,
        "CPF": "55641815063",
        "card": "3123****7687",
        "hour": "2019-03-01T04:56:07Z",
        "company": 2
      },
      {
        "id": 9,
        "type": 1,
        "date": "2019-03-01",
        "value": 200.0,
        "CPF": "55641815063",
        "card": "1234****3324",
        "hour": "2019-03-01T09:00:02Z",
        "company": 2
      }
    ],
    "account_balance": 460.0,
    "store_owner": "MARIA JOSEFINA",
    "store_name": "LOJA DO Ó - MATRIZ"
  }
]
```

#### `GET api/companies/store_id - FORMATO DE REQUISIÇÃO`

```json
Vazio
```

#### `GET api/companies/store_id - FORMATO DE RESPOSTA - STATUS 200`

```json
{
  "id": 1,
  "transactions": [
    {
      "id": 1,
      "type": 3,
      "date": "2019-03-01",
      "value": 142.0,
      "CPF": "09620676017",
      "card": "4753****3153",
      "hour": "2019-03-01T05:34:53Z",
      "company": 1
    }
  ],
  "account_balance": -204.0,
  "store_owner": "JOÃO MACEDO",
  "store_name": "BAR DO JOÃO"
}
```
