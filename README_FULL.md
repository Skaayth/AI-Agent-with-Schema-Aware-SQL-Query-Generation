# 🧠 Building AI Agents for the Enterprise - Schema-Aware AI SQL Agent
> 💡 This project runs locally using Python, FastAPI, and Streamlit. You can connect it to any SQL-compatible database or use the built-in Northwind sample via Docker.  
> Setup typically takes **5-10 minutes** and requires **basic command-line usage**.  
> You'll configure `.env` and `config.yaml` to match your environment and optionally run a provided PostgreSQL container for fast onboarding.

## 📚 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Real-World Use Cases](#-real-world-use-cases)
- [Modes of Operation](#-modes-of-operation)
- [Technologies Used](#-technologies-used)
- [Architecture Highlights](#-architecture-highlights)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
  - [1 Prerequisites](#1-prerequisites)
  - [2 Installation](#2-installation)
  - [3 env File Setup](#3-env-file-setup)
  - [4 Config File Setup](#4-config-file-setup)
  - [5 Database Setup](#5-database-setup)
- [Running the Backend](#-running-the-backend)
- [Running the Frontend](#-running-the-frontend)
- [Accessing the Application](#-accessing-the-application)
- [Backend README](#-backend-readme)
- [Frontend README](#-frontend-readme)
- [Contributing](#-contributing)
- [Questions](#-questions)
- [License](#-license)
- [Security Considerations: Schema Exposure](#-security-considerations-schema-exposure)
- [Coming Soon / Future Enhancements](#-coming-soon--future-enhancements)

> 💡 Tip: To preview this file locally in VS Code or editors supporting markdown content, use <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> (or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> on Windows).

---

## 🔍 Overview

The **Schema-Aware AI SQL Agent** is a production-grade system that translates natural language into safe, executable SQL queries — without blindly trusting the LLM. Designed for enterprise environments, it enforces schema awareness, RBAC, RLS, and SQL sanitization to ensure compliance, correctness, and security. 

Built with open-source tools like **LangChain**, **FastAPI**, and **Streamlit**, the solution combines AI flexibility with traditional software principles to deliver a reliable, extensible, and governance-ready interface for querying structured data.

---

## 🎯 Key Features

- 💬 Natural language to SQL generation using LLMs
- 🔐 Built-in guardrails: schema validation, RBAC, RLS, query sanitization, and prompt engineering
- 🚀 REST API and interactive Chat UI for flexible access
- 🔄 Supports both stateless API and stateful agent modes (toggle in UI)
- 🗃️ Includes sample database schema (Northwind) for testing and onboarding
- 🧩 Modular backend architecture designed for enterprise extensibility
- ⚙️ Extensible & Configurable – Easily switch LLM models and database configurations
- ⚡ Real-Time Execution & Performance Optimization – Designed for low-latency environments

---

## 💼 Real-World Use Cases

- Business Intelligence Portals — Enable non-technical users to explore data within governed, role-restricted boundaries
- Internal Tools for Data Teams — Streamline analyst and operations workflows while maintaining strict access controls
- Customer Support Dashboards — Allow support agents to retrieve contextual data using natural language, without writing SQL
- Data Validation & Reconciliation — Detect anomalies, check totals, or validate consistency using conversational queries
- AI-Augmented Dev & QA — Assist developers and testers in understanding and debugging datasets through natural language prompts
- AI-Powered SQL Assistants — Support data engineering and ML workflows with secure, schema-aware SQL generation
- Secure Self-Service Data Access — Empower business users to generate SQL queries within defined governance and access boundaries
- Compliance-Aware Querying — Enforce RBAC/RLS and access rules directly in query generation for audit readiness and regulated environments
- Automated BI Workflows — Generate and execute SQL queries to power dashboards, reports, or scheduled pipelines
- Data Stewardship Tools — Help governance teams review and refine access boundaries through agent-assisted querying
- Ad Hoc Exploration for Executives — Let decision-makers ask structured questions without needing analysts or SQL knowledge

---

## 🧠 Modes of Operation

This project supports two modes of query generation:

- **API Mode (`/ask`)** – Stateless, single-turn query generation.
- **AI Agent Mode (`/chat`)** – Stateful, memory-aware conversations.

Switch between them using the toggle in the frontend UI.

---

## 🛠 Technologies Used

- **Python 3.10+**
- **FastAPI** – high-performance REST backend
- **Streamlit** – chat UI for natural language interaction
- **SQLAlchemy** – database abstraction across SQL engines
- **LangChain** – LLM orchestration and prompt flows
- **OpenAI / OpenRouter / Ollama** – LLM providers
- **PostgreSQL** – sample database (Northwind)
- **Docker & Docker Compose** – for quick local setup

---

## 📐 Architecture Highlights

Here’s a high-level look at how the system works—from UI to LLM to SQL execution.

![System Architecture](assets/System-Architecture.jpg)

*The system is composed of three main layers:*

- **Frontend (using Streamlit)** – Provides an interactive UI for asking natural language questions and viewing SQL + results.
- **Backend (using FastAPI)** – Hosts the API endpoints (`/ask`, `/chat`) that handle query processing, memory, LLM routing, and role enforcement.
- **Database** – An SQL-compatible engine (e.g., PostgreSQL) connected via SQLAlchemy, with schema introspection and security rules applied.

This modular architecture separates AI logic, user access, and data governance—making it adaptable to enterprise needs and secure by design.

### 🧠 Functionality

- `/ask` — direct, stateless query generation
- `/chat` — multi-turn conversational query generation with memory
- LLM Integration — prompt injection protection and sanitization
- RBAC — table/column-level enforcement
- Schema-Aware Execution — validates schema, foreign keys, constraints
- Clarification Flow — detects vague prompts and asks follow-ups

### 🔐 Security & Governance Model

- Enforces and simulates RBAC rules defined in `config.yaml`. These rules are hardcoded for demonstration — in a production system, they would be dynamically fetched from your IAM or access policy service.
- Blocks unsafe queries using SQL sanitization
- Detects hallucinations and responds gracefully
- Simulates RLS rules defined in `config.yaml`. These are demonstration rules — in a production system, RLS logic would typically be enforced by your database engine or a centralized policy engine.

### 🛠️ Configuration and IAM Notes

- `config.yaml` contains role mappings and access policies
- In production, these values should be fetched from your IAM provider (e.g., Okta, Azure AD)
- `authenticate_user()` is a placeholder — replace with real identity checks in production

---

## 🗂 Project Structure

```
AI-Agent-with-Schema-Aware-SQL-Query-Generation/
├── backend/
│   ├── agent/                 # AI agent logic and memory
│   ├── api/                   # FastAPI entry point and route definitions
│   └── utils/                 # Configuration, logging, and utility functions
│       └── config.yaml        # Access rules and system behavior
├── database/                  # Schema parsing and SQL generation logic
├── frontend/                  # Streamlit chat interface
├── docker/                    # Docker Compose setup for the sample Postgres DB
│   └── .env.example           # Sample Docker environment variables
├── requirements.txt           # Project dependencies
├── .env.example               # Sample environment variable file
├── README.md                  # Main documentation
└── README_FULL.md             # Full documentation
```

---

## ⚙ Setup Instructions
_Follow these steps to get the system running locally. You can connect to your own database or use the provided Northwind sample._

### 1️⃣ Prerequisites

- Python 3.10+
- Streamlit (installed via `requirements.txt`)
- SQL-compatible database (PostgreSQL, MySQL, SQL Server, etc.)
- OpenAI or local-compatible LLM provider
- Docker (optional for running the sample Northwind DB)

---

### 2️⃣ Installation

```bash
git clone https://github.com/Skaayth/AI-Agent-with-Schema-Aware-SQL-Query-Generation.git
cd AI-Agent-with-Schema-Aware-SQL-Query-Generation
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3️⃣ .env File Setup

```bash
cp .env.example .env
```

Update `.env` (located in the root directory) with:

- `DATABASE_URL` – your database connection string
- `OPENAI_API_KEY` – if using OpenAI
- `OPENROUTER_API_KEY` – if using OpenRouter
- Additional provider-specific values as needed

---

### 4️⃣ Config File Setup

Update `backend/utils/config.yaml` to match your environment:

- `RBAC_RULES`, `RLS_RULES`, `SENSITIVE_COLUMNS`
- `LLM_PROVIDER`, model name
- `USER_SETTINGS` for simulated login identity

If you're using the Northwind sample database, no changes are required.

---


### 5️⃣ 🗄️ Database Setup

You can connect to your own database or use the provided Northwind schema in PostgreSQL, with or without Docker.

To get started quickly, we recommend using the **included Dockerized PostgreSQL database with the Northwind sample schema**. It allows you to explore the system's features (RBAC, RLS, prompt engineering, SQL sanitization) with minimal setup.

Once you're comfortable, you can switch to your own database by updating your `.env` and `config.yaml` files.

---

#### 🔹 Option 1: Use Your Own Database  
_Connect to any SQL-compatible database (PostgreSQL, MySQL, SQL Server, etc.) and bring your own schema._

1. Set `DATABASE_URL` in your `.env` file.  
2. Update the following in `backend/utils/config.yaml`:
   - `RBAC_RULES`
   - `RLS_RULES`
   - `SENSITIVE_COLUMNS`

---

#### 🔹 Option 2: Use Your PostgreSQL + Northwind Sample Schema  
_Load the Northwind schema into your own PostgreSQL instance._

1. Run the database script to create the schema and seed data:

```bash
psql -U youruser -d yourdb -f database/northwind.sql
```

2. Set your `.env` file:

```env
DATABASE_URL=postgresql://youruser:yourpassword@localhost:5432/northwind
```

#### 🐳 Option 3: Use Docker for Prebuilt PostgreSQL, northwind database and sample data  
_Spin up a local PostgreSQL container with the Northwind schema already loaded._

If you’re using this option, no manual database setup is needed.
The container will automatically create:

	•	The northwind database
	•	The northwind_user with password northwind_pass


1. Make sure your root `.env` (copied from `.env.example`) includes the `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` values — these are read by `docker-compose.yml` to provision the container. The defaults match `docker/.env.example`.

2. Navigate to the `docker` folder and run:

```bash
cd docker
docker-compose up -d
```

3. Your root `.env` file should already have this line:

```env
DATABASE_URL=postgresql://northwind_user:northwind_pass@localhost:5432/northwind
```

---

## 🚀 Running the Backend

```bash
uvicorn backend.api.api:app --host 127.0.0.1 --port 8000 --reload
```

> 🔧 This starts the FastAPI server with live reload.

Access the interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💻 Running the Frontend

```bash
python3 -m streamlit run frontend/chat_UI.py
```

> 💬 This launches the natural language UI in your browser.

---

## 🖥 Accessing the Application

Once both backend and frontend are running, visit:

[http://localhost:8501](http://localhost:8501) — for the Chat UI  
[http://localhost:8000/docs](http://localhost:8000/docs) — for interactive API access via Swagger UI  

---

### ✅ Setup Complete

If you're seeing the **Chat UI** at [http://localhost:8501](http://localhost:8501) and the **FastAPI docs** at [http://localhost:8000/docs](http://localhost:8000/docs), your system is up and running.


## 🗄 Backend README

<details>
<summary><strong>Click to expand</strong></summary>

### Backend Overview

- FastAPI-powered API
- Converts natural language into secure SQL
- Supports multiple LLM providers

#### Key Components

- `api.py` – FastAPI app
- `llm_client.py` – LLM abstraction
- `schema_aware_sql.py` – schema validation engine
- `utils.py` – auth and helper functions

#### API Endpoints

- `POST /ask` – stateless SQL generation
- `POST /chat` – conversational agent with memory

#### Run Locally

```bash
uvicorn backend.api.api:app --host 127.0.0.1 --port 8000 --reload
```

</details>

---

## 🎨 Frontend README

<details>
<summary><strong>Click to expand</strong></summary>

### Frontend Overview

- Built with Streamlit
- Chat-style interface for natural language SQL
- Displays SQL and results side-by-side

#### Run Locally

```bash
python3 -m streamlit run frontend/chat_UI.py
```

#### Customization

Edit `chat_demo.py` to modify UI layout, prompt formats, or model selectors.

</details>

---

## 🤝 Contributing

If you have questions, ideas, or feedback — open a GitHub issue. We welcome contributions.

---

## 📬 Questions?

Open an issue on GitHub.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🎯 Security Considerations: Schema Exposure

While this system does not share user data with LLMs, it does expose database schema metadata to generate SQL. This includes:

Table names

Column names

Relationships and keys

To mitigate schema exposure:

Option 1 – Schema Filtering (Recommended)Use the config file to filter sensitive tables or columns before they are included in LLM prompts.

Option 2 – Local LLMs (Best for Privacy)Run the agent using a local LLM (e.g., Ollama or LM Studio) to ensure prompts and schema never leave your environment.

---

## 🧪 Coming Soon / Ideas / Potential Enhancements

Below are areas we’re exploring for future iterations — depending on usage, feedback, and interest:

- ✅ Vector-based schema retrieval (RAG)
- ✅ Fine-tuned LLM support
- 🚧 OpenAPI-based schema parsing
- 🚧 Multi-turn clarification engine
- 🚧 Adaptive query optimization
- 🚧 Personalized query recommendations
- 🚧 Natural language SQL tuning (e.g., “make this query faster”)
- 🚧 Query caching and smart autocomplete
- 🚧 Inline data visualizations and basic analytics

---

> 💡 Tip: To preview this file locally in VS Code or editors supporting markdown content, use <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> (or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> on Windows).
