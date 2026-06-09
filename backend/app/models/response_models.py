from typing import Dict, List

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str


class InferenceResponse(BaseModel):
    request_id: str
    prompt: str
    response: str
    selected_provider: str
    routing_mode: str
    routing_reason: str
    cache_hit: bool
    retry_count: int
    latency_ms: int
    input_tokens: int
    output_tokens: int
    estimated_cost: float
    timestamp: str


class MetricsResponse(BaseModel):
    total_requests: int
    cache_hits: int
    cache_hit_rate: float
    average_latency_ms: int
    total_estimated_cost: float
    provider_usage: Dict[str, int]
    recent_requests: List[InferenceResponse]
