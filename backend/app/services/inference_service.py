from datetime import datetime, timezone
from random import randint

from app.models.request_models import InferenceRequest
from app.models.response_models import InferenceResponse
from app.services.cache_service import cache_service
from app.services.mock_provider_service import mock_provider_service
from app.services.routing_service import routing_service
from app.utils.id_utils import create_request_id
from app.utils.token_utils import estimate_cost, estimate_tokens


class InferenceService:
    def run_inference(self, request: InferenceRequest) -> InferenceResponse:
        cached_result = cache_service.find_match(request.prompt)
        input_tokens = estimate_tokens(request.prompt)

        if cached_result:
            output_tokens = estimate_tokens(cached_result.response)
            return InferenceResponse(
                request_id=create_request_id(),
                prompt=request.prompt,
                response=cached_result.response,
                selected_provider=cached_result.selected_provider,
                routing_mode=request.routing_mode,
                routing_reason="Semantic cache hit: a similar prompt was already answered, so InferFlow skipped a model call.",
                cache_hit=True,
                retry_count=0,
                latency_ms=randint(35, 95),
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                estimated_cost=0,
                timestamp=self._timestamp(),
            )

        provider, routing_reason = routing_service.select_provider(request.routing_mode)
        provider_result = mock_provider_service.invoke(provider, request.prompt)
        output_tokens = provider_result["output_tokens"]
        estimated_cost = estimate_cost(input_tokens, output_tokens, provider.cost_per_1k_tokens)

        response = InferenceResponse(
            request_id=create_request_id(),
            prompt=request.prompt,
            response=provider_result["response"],
            selected_provider=provider.name,
            routing_mode=request.routing_mode,
            routing_reason=routing_reason,
            cache_hit=False,
            retry_count=provider_result["retry_count"],
            latency_ms=provider_result["latency_ms"],
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            estimated_cost=estimated_cost,
            timestamp=self._timestamp(),
        )

        cache_service.add(request.prompt, response.response, provider.name)
        return response

    def _timestamp(self) -> str:
        return datetime.now(timezone.utc).isoformat()


inference_service = InferenceService()
