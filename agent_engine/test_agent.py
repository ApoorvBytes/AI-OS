from agent_engine.agent import Agent
from ai_core.tool_registry import Tool, ToolRegistry
from system_services.permissions import RiskLevel, PermissionManager


def get_system_info():
    return {
        "operating_system": "Windows",
        "architecture": "AMD64",
    }


def test_agent_can_execute_low_risk_tool():
    registry = ToolRegistry()

    registry.register(
        Tool(
            name="get_system_info",
            description="Get basic system information",
            risk_level="LOW",
            execute=get_system_info,
        )
    )

    permissions = PermissionManager()

    agent = Agent(
        tool_registry=registry,
        permission_manager=permissions,
    )

    result = agent.execute_tool(
        tool_name="get_system_info",
        risk_level=RiskLevel.LOW,
        reason="User requested system information",
    )

    assert result.success is True
    assert result.tool_name == "get_system_info"
    assert result.result["operating_system"] == "Windows"


def test_agent_blocks_high_risk_tool():
    registry = ToolRegistry()

    registry.register(
        Tool(
            name="delete_file",
            description="Delete a file",
            risk_level="HIGH",
            execute=lambda: "deleted",
        )
    )

    permissions = PermissionManager()

    agent = Agent(
        tool_registry=registry,
        permission_manager=permissions,
    )

    result = agent.execute_tool(
        tool_name="delete_file",
        risk_level=RiskLevel.HIGH,
        reason="Delete requested file",
    )

    assert result.success is False
    assert result.error == "Permission denied."


if __name__ == "__main__":
    test_agent_can_execute_low_risk_tool()
    test_agent_blocks_high_risk_tool()

    print("Agent engine tests passed.")