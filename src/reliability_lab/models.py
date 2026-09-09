from enum import Enum
from pydantic import BaseModel, Field


class FailureType(str, Enum):
    NONE = "none"
    TIMEOUT = "timeout"
    RATE_LIMIT = "rate_limit"
    SERVER_ERROR = "server_error"
    MALFORMED_RESPONSE = "malformed_response"
    WRONG_RESPONSE = "wrong_response"


class ToolRisk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class FailureScenario(BaseModel):
    failure_type: FailureType = FailureType.NONE
    probability: float = Field(default=0.0, ge=0.0, le=1.0)
    target: str = "search"


class PolicyDecision(BaseModel):
    allowed: bool
    requires_approval: bool
    reason: str


class RunResult(BaseModel):
    scenario: str
    success: bool
    status: str
    attempts: int
    retries: int
    latency_ms: float
    estimated_cost: float
    failure: str | None = None
