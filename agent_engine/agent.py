from dataclasses import dataclass
from typing import Any

from ai_core.tool_registry import ToolRegistry
from system_services.permissions import (
    PermissionManager,
    PermissionRequest,
    RiskLevel,
)

@dataclass
class AgentResult:
    success: bool
    tool_name: str
    result: Any = None
    error: str | None = None


class Agent:
    """Basic AI OS agent that executes approved capabilities."""

    def __init__(
        self,
        tool_registry: ToolRegistry,
        permission_manager: PermissionManager,
    ) -> None:
        self.tool_registry = tool_registry
        self.permission_manager = permission_manager

    def execute_tool(
        self,
        tool_name: str,
        risk_level: RiskLevel,
        reason: str,
    ) -> AgentResult:

        try:
            tool = self.tool_registry.get(tool_name)
        except KeyError as error:
            return AgentResult(
                success=False,
                tool_name=tool_name,
                error=str(error),
            )

        permission_request = PermissionRequest(
            tool_name=tool_name,
            risk_level=risk_level,
            reason=reason,
        )

        if not self.permission_manager.request(permission_request):
            return AgentResult(
                success=False,
                tool_name=tool_name,
                error="Permission denied.",
            )

        try:
            result = tool.execute()

            return AgentResult(
                success=True,
                tool_name=tool_name,
                result=result,
            )

        except Exception as error:
            return AgentResult(
                success=False,
                tool_name=tool_name,
                error=f"Tool execution failed: {error}",
            )