from ai_core.intent import IntentParser
from ai_core.tool_registry import Tool, ToolRegistry
from agent_engine.agent import Agent
from agent_engine.orchestrator import Orchestrator
from system_services.permissions import PermissionManager
from system_services.system_info import SystemInfoTool


def build_orchestrator() -> Orchestrator:
    """Build the AI OS core pipeline."""

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

    permission_manager = PermissionManager()

    agent = Agent(
        tool_registry=registry,
        permission_manager=permission_manager,
    )

    intent_parser = IntentParser()

    return Orchestrator(
        intent_parser=intent_parser,
        agent=agent,
    )


def main() -> None:
    orchestrator = build_orchestrator()

    print()
    print("=" * 50)
    print("                 AI OS")
    print("            Core Prototype v0.1")
    print("=" * 50)
    print()
    print("Type a command or type 'exit' to quit.")
    print()

    while True:
        try:
            user_input = input("ai-os> ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\nExiting AI OS.")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Shutting down AI OS.")
            break

        result = orchestrator.handle(user_input)

        if result.success:
            print()
            print("AI OS:")
            print(result.result)
            print()
        else:
            print()
            print(f"AI OS: {result.error}")
            print()


if __name__ == "__main__":
    main()