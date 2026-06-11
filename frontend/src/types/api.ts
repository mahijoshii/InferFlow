export type RoutingMode = "fastest" | "cheapest" | "highest_quality" | "balanced";

export type Provider = {
  name: string;
  speed: string;
  base_latency_ms: number;
  cost_per_1k_tokens: number;
  reliability: number;
  quality_score: number;
  best_use_case: string;
  color: string;
};

export type InferenceResponse = {
  request_id: string;
  prompt: string;
  response: string;
  selected_provider: string;
  routing_mode: RoutingMode;
  routing_reason: string;
  cache_hit: boolean;
  retry_count: number;
  latency_ms: number;
  input_tokens: number;
  output_tokens: number;
  estimated_cost: number;
  timestamp: string;
};

export type MetricsResponse = {
  total_requests: number;
  cache_hits: number;
  cache_hit_rate: number;
  average_latency_ms: number;
  total_estimated_cost: number;
  provider_usage: Record<string, number>;
  recent_requests: InferenceResponse[];
};
