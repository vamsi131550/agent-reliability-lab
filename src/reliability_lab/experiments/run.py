import argparse
from reliability_lab.agents.agent import ReliabilityAgent
from reliability_lab.models import FailureScenario, FailureType


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="tool_timeout")
    parser.add_argument("--iterations", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    mapping = {
        "tool_timeout": FailureType.TIMEOUT,
        "rate_limit": FailureType.RATE_LIMIT,
        "server_error": FailureType.SERVER_ERROR,
        "malformed_response": FailureType.MALFORMED_RESPONSE,
    }
    failure = mapping.get(args.scenario, FailureType.NONE)
    agent = ReliabilityAgent(seed=args.seed)

    successes = 0
    for i in range(args.iterations):
        result = agent.run(
            FailureScenario(
                failure_type=failure,
                probability=0.4,
                target="search",
            )
        )
        successes += result.success
        print(
            f"run={i+1:03d} status={result.status} "
            f"attempts={result.attempts} retries={result.retries} "
            f"latency_ms={result.latency_ms:.2f}"
        )

    print(f"\ncompletion_rate={successes / args.iterations:.2%}")


if __name__ == "__main__":
    main()
