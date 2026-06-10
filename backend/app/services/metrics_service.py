from collections import Counter

from app.data.providers import PROVIDERS
from app.models.response_models import InferenceResponse, MetricsResponse


class MetricsService:
    def __init__(self):
        self.requests: list[InferenceResponse] = []

    def record(self, result: InferenceResponse) -> None:
        self.requests.append(result)

    def get_metrics(self) -> MetricsResponse:
        total_requests = len(self.requests)
        cache_hits = sum(1 for request in self.requests if request.cache_hit)
        total_latency = sum(request.latency_ms for request in self.requests)
        total_cost = sum(request.estimated_cost for request in self.requests)
        provider_counts = Counter(request.selected_provider for request in self.requests)

        return MetricsResponse(
            total_requests=total_requests,
            cache_hits=cache_hits,
            cache_hit_rate=round(cache_hits / total_requests, 2) if total_requests else 0,
            average_latency_ms=round(total_latency / total_requests) if total_requests else 0,
            total_estimated_cost=round(total_cost, 4),
            provider_usage={provider.name: provider_counts.get(provider.name, 0) for provider in PROVIDERS},
            recent_requests=list(reversed(self.requests[-8:])),
        )

    def clear(self) -> None:
        self.requests.clear()


metrics_service = MetricsService()
