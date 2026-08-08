from ai_core.intent import IntentParser
from ai_core.tool_registry import Tool, ToolRegistry
from agent_engine.agent import Agent
from agent_engine.orchestrator import Orchestrator
from system_services.permissions import PermissionManager
from system_services.system_info import SystemInfoTool


def build_orchestrator():
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

    parser = IntentParser()

    return Orchestrator(
        intent_parser=parser,
        agent=agent,
    )


def test_end_to_end_system_information():
    orchestrator = build_orchestrator()

    result = orchestrator.handle(
        "Show me my system information"
    )

    assert result.success is True
    assert result.intent == "get_system_info"
    assert result.result.operating_system
    assert result.result.architecture

    print("End-to-end AI OS test passed.")
    print(f"OS: {result.result.operating_system}")
    print(f"Architecture: {result.result.architecture}")


def test_unknown_request():
    orchestrator = build_orchestrator()

    result = orchestrator.handle(
        "Make me a sandwich"
    )

    assert result.success is False
    assert result.intent == "unknown"

    print("Unknown request correctly rejected.")


if __name__ == "__main__":
    test_end_to_end_system_information()
    test_unknown_request()

    print("Orchestrator tests passed.")