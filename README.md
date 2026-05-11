# LangGraph Groq Summarizer Agent

An AI-powered text summarization agent built using **LangGraph**, **LangChain**, **Groq API**, and **FastAPI**.

This project follows a modular workflow architecture using:
- `state.py`
- `nodes.py`
- `graph_builder.py`

The agent accepts text input and generates concise summaries using Groq LLM models.

---

# Features

- LangGraph workflow orchestration
- LangChain + Groq integration
- FastAPI REST API
- Docker support
- YAML-based agent configuration
- Environment variable support
- Marketplace validation compatible
- Modular graph architecture

---

# Project Structure

```bash
execution/
│
├── agent.yaml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
├── main.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── graph_builder.py


Installation Steps
1. Clone Repository
git clone https://github.com/sivan-droid/execution.git
cd execution
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory.

Example
GROQ_API_KEY=your_groq_api_key_here
5. Run the Application
uvicorn main:app --reload
Server URL
http://127.0.0.1:8000
