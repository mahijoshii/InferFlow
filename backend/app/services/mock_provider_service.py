import random

from app.models.provider_models import Provider
from app.utils.token_utils import estimate_tokens


class MockProviderService:
    def invoke(self, provider: Provider, prompt: str) -> dict:
        retry_count = 0
        latency_ms = self._simulate_latency(provider)

        if self._request_failed(provider):
            retry_count = 1
            latency_ms += self._simulate_latency(provider)

        response = self._generate_response(provider, prompt, retry_count)
        output_tokens = estimate_tokens(response)

        return {
            "response": response,
            "retry_count": retry_count,
            "latency_ms": latency_ms,
            "output_tokens": output_tokens,
        }

    def _simulate_latency(self, provider: Provider) -> int:
        variation = random.randint(-90, 220)
        return max(80, provider.base_latency_ms + variation)

    def _request_failed(self, provider: Provider) -> bool:
        return random.random() > provider.reliability

    def _generate_response(self, provider: Provider, prompt: str, retry_count: int) -> str:
        retry_note = " The first attempt failed, but the retry recovered cleanly." if retry_count else ""
        prompt_preview = prompt.strip().replace("\n", " ")[:120]

        return (
            f"{provider.name} handled this prompt with a {provider.quality_score}/100 quality profile. "
            f"It interpreted the request as: \"{prompt_preview}\". "
            "In a real gateway, this is where the selected LLM response would appear."
            f"{retry_note}"
        )


mock_provider_service = MockProviderService()
