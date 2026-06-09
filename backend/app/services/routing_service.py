from app.data.providers import PROVIDERS
from app.models.provider_models import Provider


class RoutingService:
    def select_provider(self, routing_mode: str) -> tuple[Provider, str]:
        if routing_mode == "fastest":
            provider = min(PROVIDERS, key=lambda item: item.base_latency_ms)
            reason = f"{provider.name} was selected because it has the lowest expected latency."
        elif routing_mode == "cheapest":
            provider = min(PROVIDERS, key=lambda item: item.cost_per_1k_tokens)
            reason = f"{provider.name} was selected because it has the lowest estimated token cost."
        elif routing_mode == "highest_quality":
            provider = max(PROVIDERS, key=lambda item: item.quality_score)
            reason = f"{provider.name} was selected because it has the highest quality score."
        else:
            provider = max(PROVIDERS, key=self._balanced_score)
            reason = (
                f"{provider.name} was selected because it provides the best tradeoff "
                "between latency, cost, reliability, and quality."
            )

        return provider, reason

    def _balanced_score(self, provider: Provider) -> float:
        latency_score = 1 - (provider.base_latency_ms / 1600)
        cost_score = 1 - (provider.cost_per_1k_tokens / 0.01)
        quality_score = provider.quality_score / 100
        return (latency_score * 0.15) + (cost_score * 0.15) + (quality_score * 0.45) + (provider.reliability * 0.25)


routing_service = RoutingService()
