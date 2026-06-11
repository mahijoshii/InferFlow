import type { InferenceResponse, MetricsResponse, Provider, RoutingMode } from "../types/api";

const API_BASE_URL = "http://localhost:8000";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export function getProviders(): Promise<Provider[]> {
  return request<Provider[]>("/providers");
}

export function runInference(prompt: string, routingMode: RoutingMode): Promise<InferenceResponse> {
  return request<InferenceResponse>("/infer", {
    method: "POST",
    body: JSON.stringify({ prompt, routing_mode: routingMode }),
  });
}

export function getMetrics(): Promise<MetricsResponse> {
  return request<MetricsResponse>("/metrics");
}

export function resetSystem(): Promise<{ status: string }> {
  return request<{ status: string }>("/reset", { method: "POST" });
}
