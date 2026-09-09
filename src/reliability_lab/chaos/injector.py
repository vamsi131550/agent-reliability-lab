import random
from reliability_lab.models import FailureScenario, FailureType


class InjectedFailure(RuntimeError):
    def __init__(self, failure_type: FailureType):
        super().__init__(failure_type.value)
        self.failure_type = failure_type


class ChaosInjector:
    def __init__(self, seed: int | None = None):
        self.random = random.Random(seed)

    def maybe_fail(self, scenario: FailureScenario, target: str) -> None:
        if scenario.target != target:
            return
        if self.random.random() > scenario.probability:
            return
        if scenario.failure_type != FailureType.NONE:
            raise InjectedFailure(scenario.failure_type)
