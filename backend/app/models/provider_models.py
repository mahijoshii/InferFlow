from pydantic import BaseModel


class Provider(BaseModel):
    name: str
    speed: str
    base_latency_ms: int
    cost_per_1k_tokens: float
    reliability: float
    quality_score: int
    best_use_case: str
    color: str
