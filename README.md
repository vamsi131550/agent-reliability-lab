# Agent Reliability Lab

A personal engineering project for testing LLM agents under controlled failures.

## Why this exists

An agent that works once is not necessarily reliable. This lab treats agent reliability as an engineering problem and measures:

- task completion
- recovery success
- latency
- retries
- policy violations
- loop detection
- estimated cost

The project intentionally injects failures into model/tool calls and compares recovery strategies.

> Personal project. Infrastructure and scenarios are synthetic; no production claims are made.

## Architecture

```text
Task
  |
  v
LangGraph-style Agent
  |
  v
Tool Registry
  |
  v
Chaos Injector
  |
  +--> timeout / rate limit / malformed response / 5xx
  |
  v
Recovery Engine
  |
  +--> retry / backoff / circuit breaker / fallback / abort
  |
  v
Evaluation
  |
  v
Metrics + traces
```

## Current starter implementation

The starter repo contains a runnable deterministic simulation of the reliability loop, fault injection, retry/backoff policy, circuit breaker, loop detection, risk policy and scenario evaluation.

The LLM adapter is intentionally provider-neutral and can be connected to an OpenAI-compatible API later.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m reliability_lab.experiments.run --scenario tool_timeout --iterations 20 --seed 42
```

Windows activation:

```powershell
.venv\Scripts\activate
```

## Suggested next iterations

1. Replace the deterministic agent with LangGraph.
2. Add an OpenAI-compatible model adapter.
3. Add MCP tools.
4. Add PostgreSQL result storage.
5. Add OpenTelemetry traces.
6. Add Prometheus/Grafana.
7. Add a benchmark dashboard.
