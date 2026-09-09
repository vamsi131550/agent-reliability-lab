# Architecture

The lab separates five concerns:

1. Agent execution
2. Fault injection
3. Recovery policy
4. Safety policy
5. Evaluation

This separation makes it possible to compare a baseline agent with increasingly resilient strategies without changing the business task itself.

## Future production-inspired additions

- LangGraph state machine
- MCP tool adapters
- OpenTelemetry traces
- Redis-backed circuit state
- PostgreSQL experiment storage
- Prometheus metrics
- Grafana dashboard
- replayable traces
- regression benchmark suite
