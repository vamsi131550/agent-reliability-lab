from reliability_lab.recovery.policies import RetryPolicy, CircuitBreaker


def test_transient_failure_is_retryable():
    p = RetryPolicy(max_retries=2)
    assert p.should_retry("timeout", 1)
    assert not p.should_retry("authorization_error", 1)


def test_circuit_breaker_opens():
    b = CircuitBreaker(threshold=2)
    b.record_failure()
    assert b.allow()
    b.record_failure()
    assert not b.allow()
