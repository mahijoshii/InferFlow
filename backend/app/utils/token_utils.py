import re


def estimate_tokens(text: str) -> int:
    words = re.findall(r"\w+", text)
    return max(1, int(len(words) * 1.3))


def estimate_cost(input_tokens: int, output_tokens: int, cost_per_1k_tokens: float) -> float:
    total_tokens = input_tokens + output_tokens
    return round((total_tokens / 1000) * cost_per_1k_tokens, 4)
