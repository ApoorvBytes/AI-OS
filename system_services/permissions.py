from dataclasses import dataclass
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(frozen=True)
class PermissionRequest:
    tool_name: str
    risk_level: RiskLevel
    reason: str


class PermissionManager:
    """Controls whether a tool may execute."""

    def __init__(self) -> None:
        self._approved_tools: set[str] = set()

    def request(self, request: PermissionRequest) -> bool:
        if request.risk_level == RiskLevel.LOW:
            return True

        return request.tool_name in self._approved_tools

    def approve(self, tool_name: str) -> None:
        self._approved_tools.add(tool_name)

    def revoke(self, tool_name: str) -> None:
        self._approved_tools.discard(tool_name)

    def is_approved(self, tool_name: str) -> bool:
        return tool_name in self._approved_tools