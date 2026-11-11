# NexaVarejo — ACP Plásticos (MVP PWA)

Sistema PWA desenvolvido para a **ACP Plásticos** com o objetivo de integrar a gestão de estoque em tempo real ao Chão de Fábrica (Kanban de Produção) e ao Atendimento Comercial.

## 🚀 Tecnologias Utilizadas
* **Backend:** Python (FastAPI, Pydantic, SQLAlchemy)
* **Banco de Dados:** PostgreSQL
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla PWA)
* **Autenticação:** JWT com hash de senhas via bcrypt
* **Acessibilidade:** WCAG 2.1 AA & Diretrizes ODS 9 (Meta 9.4)

## 📁 Estrutura do Repositório
* `app/`: Regras de negócio, endpoints FastAPI e modelos de dados.
* `tests/`: Testes unitários e de integração automatizados (PyTest).
* `static/`: Telas e componentes visuais do PWA.
* `.github/workflows/`: Pipeline de Integração Contínua (CI).

## 🧪 Como Executar os Testes
```bash
pip install -r requirements.txt
pytest

<!-- Revisão de PR -->
