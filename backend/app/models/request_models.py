from typing import Literal

from pydantic import BaseModel, Field

RoutingMode = Literal["fastest", "cheapest", "highest_quality", "balanced"]


class InferenceRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)
    routing_mode: RoutingMode = "balanced"
