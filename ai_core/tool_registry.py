from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Tool:
    """Definition of a capability available to AI OS."""

    name: str
    description: str
    risk_level: str
    execute: Callable[..., Any]


class ToolRegistry:
    """Central registry for AI OS capabilities."""

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")

        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise KeyError(f"Tool not found: {name}")

        return self._tools[name]

    def list_tools(self) -> list[Tool]:
        return list(self._tools.values())