# API Transportadora Parceira (SQLite)

## Requisitos
- Python 3.9+
- SQLite
- FastAPI

## Instalação

```bash
pip install -r requirements.txt
```

## Rodando o projeto

```bash
uvicorn app.main:app --reload
```

Use o header `x-api-key` com a chave definida em `dependencies.py`.
