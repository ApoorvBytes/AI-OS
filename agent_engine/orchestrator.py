from dataclasses import dataclass
from typing import Any

from ai_core.intent import IntentParser
from ai_core.tool_registry import ToolRegistry
from agent_engine.agent import Agent
from system_services.permissions import PermissionManager, RiskLevel


@dataclass
class OrchestratorResult:
    success: bool
    intent: str
    result: Any = None
    error: str | None = None


class Orchestrator:
    """Connects user intent to the appropriate AI OS capability."""

    def __init__(
        self,
        intent_parser: IntentParser,
        agent: Agent,
    ) -> None:
        self.intent_parser = intent_parser
        self.agent = agent

    def handle(self, user_input: str) -> OrchestratorResult:
        intent = self.intent_parser.parse(user_input)

        if intent.name == "unknown":
            return OrchestratorResult(
                success=False,
                intent="unknown",
                error="I don't understand that request yet.",
            )

        if intent.name == "get_system_info":
            result = self.agent.execute_tool(
                tool_name="get_system_info",
                risk_level=RiskLevel.LOW,
                reason="User requested system information",
            )

            return OrchestratorResult(
                success=result.success,
                intent=intent.name,
                result=result.result,
                error=result.error,
            )

        return OrchestratorResult(
            success=False,
            intent=intent.name,
            error="No handler exists for this intent.",
        )