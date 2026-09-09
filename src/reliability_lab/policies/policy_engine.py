from reliability_lab.models import PolicyDecision, ToolRisk


class PolicyEngine:
    def decide(self, risk: ToolRisk) -> PolicyDecision:
        if risk == ToolRisk.CRITICAL:
            return PolicyDecision(
                allowed=False,
                requires_approval=False,
                reason="Critical operations are denied."
            )
        if risk == ToolRisk.HIGH:
            return PolicyDecision(
                allowed=True,
                requires_approval=True,
                reason="High-risk operation requires human approval."
            )
        return PolicyDecision(
            allowed=True,
            requires_approval=False,
            reason="Operation is within autonomous policy."
        )
