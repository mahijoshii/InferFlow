from app.models.provider_models import Provider

PROVIDERS = [
    Provider(
        name="FlashLite",
        speed="Fastest",
        base_latency_ms=360,
        cost_per_1k_tokens=0.0018,
        reliability=0.96,
        quality_score=72,
        best_use_case="Low-latency summaries and simple transformations",
        color="#38bdf8",
    ),
    Provider(
        name="BalancedAI",
        speed="Medium",
        base_latency_ms=760,
        cost_per_1k_tokens=0.0032,
        reliability=0.98,
        quality_score=84,
        best_use_case="General product features and everyday assistant tasks",
        color="#a78bfa",
    ),
    Provider(
        name="DeepReason",
        speed="Slower",
        base_latency_ms=1280,
        cost_per_1k_tokens=0.0085,
        reliability=0.97,
        quality_score=95,
        best_use_case="Reasoning-heavy analysis and technical explanations",
        color="#f97316",
    ),
    Provider(
        name="CheapChat",
        speed="Fast",
        base_latency_ms=620,
        cost_per_1k_tokens=0.0009,
        reliability=0.88,
        quality_score=66,
        best_use_case="Cost-sensitive drafts and classification tasks",
        color="#22c55e",
    ),
]
