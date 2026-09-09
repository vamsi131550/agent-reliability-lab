import time
from dataclasses import dataclass


TRANSIENT = {"timeout", "rate_limit", "server_error"}


@dataclass
class RetryPolicy:
    max_retries: int = 2
    base_delay: float = 0.02

    def should_retry(self, failure: str, attempt: int) -> bool:
        return failure in TRANSIENT and attempt <= self.max_retries

    def delay(self, attempt: int) -> float:
        return self.base_delay * (2 ** max(attempt - 1, 0))


class CircuitBreaker:
    def __init__(self, threshold: int = 3):
        self.threshold = threshold
        self.failures = 0
        self.open = False

    def record_success(self):
        self.failures = 0
        self.open = False

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.open = True

    def allow(self) -> bool:
        return not self.open
