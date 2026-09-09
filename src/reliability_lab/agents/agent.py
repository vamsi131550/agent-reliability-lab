import time
from reliability_lab.chaos.injector import ChaosInjector, InjectedFailure
from reliability_lab.models import FailureScenario, RunResult
from reliability_lab.recovery.policies import RetryPolicy, CircuitBreaker


class ReliabilityAgent:
    def __init__(self, seed: int = 42):
        self.chaos = ChaosInjector(seed)
        self.retry = RetryPolicy()
        self.breaker = CircuitBreaker()

    def run(self, scenario: FailureScenario, iterations: int = 1) -> RunResult:
        start = time.perf_counter()
        attempts = 0
        retries = 0
        last_failure = None

        for _ in range(iterations):
            while True:
                attempts += 1
                if not self.breaker.allow():
                    return RunResult(
                        scenario=scenario.failure_type.value,
                        success=False,
                        status="circuit_open",
                        attempts=attempts,
                        retries=retries,
                        latency_ms=(time.perf_counter() - start) * 1000,
                        estimated_cost=attempts * 0.001,
                        failure=last_failure,
                    )
                try:
                    self.chaos.maybe_fail(scenario, scenario.target)
                    self.breaker.record_success()
                    return RunResult(
                        scenario=scenario.failure_type.value,
                        success=True,
                        status="completed",
                        attempts=attempts,
                        retries=retries,
                        latency_ms=(time.perf_counter() - start) * 1000,
                        estimated_cost=attempts * 0.001,
                    )
                except InjectedFailure as exc:
                    last_failure = exc.failure_type.value
                    self.breaker.record_failure()
                    if not self.retry.should_retry(last_failure, attempts):
                        return RunResult(
                            scenario=scenario.failure_type.value,
                            success=False,
                            status="failed",
                            attempts=attempts,
                            retries=retries,
                            latency_ms=(time.perf_counter() - start) * 1000,
                            estimated_cost=attempts * 0.001,
                            failure=last_failure,
                        )
                    retries += 1
                    time.sleep(self.retry.delay(retries))
