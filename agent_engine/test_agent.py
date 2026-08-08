from agent_engine.agent import Agent
from ai_core.tool_registry import Tool, ToolRegistry
from system_services.permissions import RiskLevel, PermissionManager
from system_services.system_info import SystemInfoTool


def test_agent_executes_real_system_tool():
    registry = ToolRegistry()

    system_info_tool = SystemInfoTool()

    registry.register(
        Tool(
            name=system_info_tool.name,
            description="Get basic system information",
            risk_level=system_info_tool.risk_level,
            execute=system_info_tool.execute,
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
    assert result.result.operating_system
    assert result.result.architecture

    print("Real system tool executed successfully.")
    print(f"OS: {result.result.operating_system}")
    print(f"Architecture: {result.result.architecture}")


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

    print("High-risk tool correctly blocked.")


if __name__ == "__main__":
    test_agent_executes_real_system_tool()
    test_agent_blocks_high_risk_tool()

    print("Agent integration tests passed.")