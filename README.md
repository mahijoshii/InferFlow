# InferFlow

**A lightweight LLM inference gateway for routing, caching, and observability.**

InferFlow is a demo-friendly full-stack project that simulates how production AI infrastructure routes prompt requests across multiple LLM providers. It helps explain key inference gateway ideas like routing policy, semantic caching, retries, latency, token usage, cost estimation, and live observability.

## Why It Matters

Real AI products often call several model backends depending on cost, latency, reliability, and quality needs. An inference gateway centralizes those decisions so teams can improve user experience, control spend, and understand system behavior.

InferFlow keeps the concept interview-friendly by using fake providers and in-memory state instead of paid APIs, databases, or external vector stores.

## Features

- Route prompts by fastest, cheapest, highest quality, or balanced mode
- Simulate model latency, reliability, retry behavior, token usage, and cost
- Detect similar prompts with a simple Jaccard semantic cache
- Return low-latency, zero-cost responses on cache hits
- Track total requests, cache hit rate, average latency, total cost, provider usage, and recent requests
- Polished React dashboard with provider cards, prompt examples, result panels, and metrics

## Architecture

```text
LLMInference/
  backend/
    app/
      data/
      models/
      services/
      utils/
      main.py
  frontend/
    src/
      api/
      components/
      types/
      App.tsx
      main.tsx
      index.css
  README.md
  .gitignore
```

## Tech Stack

- Backend: Python, FastAPI, Pydantic, Uvicorn
- Frontend: React, TypeScript, Vite, plain CSS
- Storage: in-memory cache and metrics

## Run Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend calls the backend at `http://localhost:8000`.

## API Endpoints

- `GET /health` - health check
- `GET /providers` - fake model provider catalog
- `POST /infer` - route a prompt and return simulated inference details
- `GET /metrics` - dashboard metrics and recent requests
- `POST /reset` - clear in-memory cache and metrics

Example request:

```json
{
  "prompt": "Explain dynamic batching in simple terms",
  "routing_mode": "balanced"
}
```

## Future Improvements

- Add streaming responses with Server-Sent Events
- Add per-provider failover routing
- Store metrics in SQLite or Postgres
- Add charts for latency and cost over time
- Replace the simple cache with embeddings and a vector database
