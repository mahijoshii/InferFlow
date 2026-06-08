# InferFlow Backend

FastAPI service for the InferFlow LLM inference gateway demo.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`
- `GET /providers`
- `POST /infer`
- `GET /metrics`
- `POST /reset`
