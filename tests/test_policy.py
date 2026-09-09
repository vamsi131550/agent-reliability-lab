from reliability_lab.models import ToolRisk
from reliability_lab.policies.policy_engine import PolicyEngine


def test_critical_is_denied():
    d = PolicyEngine().decide(ToolRisk.CRITICAL)
    assert not d.allowed


def test_high_requires_approval():
    d = PolicyEngine().decide(ToolRisk.HIGH)
    assert d.allowed
    assert d.requires_approval
