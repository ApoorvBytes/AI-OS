from tool_registry import Tool, ToolRegistry


def get_system_info():
    return {"status": "ok"}


def test_tool_registry():
    registry = ToolRegistry()

    tool = Tool(
        name="get_system_info",
        description="Get basic system information",
        risk_level="LOW",
        execute=get_system_info,
    )

    registry.register(tool)

    registered_tool = registry.get("get_system_info")

    assert registered_tool.name == "get_system_info"
    assert registered_tool.risk_level == "LOW"
    assert registered_tool.execute() == {"status": "ok"}

    tools = registry.list_tools()

    assert len(tools) == 1

    print("Tool registry test passed.")


if __name__ == "__main__":
    test_tool_registry()