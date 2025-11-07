# 📝 dio_blog_fastapi

Um projeto de exemplo com **FastAPI**, **Poetry**, **Pydantic**, **Alembic** e **pytest**, seguindo boas práticas de organização em `src/`.

---

## 🚀 Instalação

1. **Instale as dependências com o Poetry:**
```bash
   poetry install
```

2. **Criar um arquivo .env:**
```bash
   cp .env.example .env
```

🧪 Executando os testes

Execute os testes com pytest dentro do ambiente virtual do Poetry:
```bash
poetry run pytest -v
```

🏗️ Estrutura do projeto
```bash
dio_blog/
├── __init__.py
└── src/
    ├── main.py
    └── ...
└── tests/
└── pyproject.toml
```