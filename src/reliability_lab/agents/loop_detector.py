class LoopDetector:
    def __init__(self, threshold: int = 3):
        self.threshold = threshold
        self.history: list[tuple[str, str]] = []

    def record(self, tool: str, arguments: str) -> None:
        self.history.append((tool, arguments))

    def detected(self) -> bool:
        if len(self.history) < self.threshold:
            return False
        return len(set(self.history[-self.threshold:])) == 1
