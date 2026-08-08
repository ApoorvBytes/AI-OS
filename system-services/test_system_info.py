from system_info import SystemInfoTool


def test_system_info():
    tool = SystemInfoTool()

    result = tool.execute()

    assert result.operating_system
    assert result.hostname
    assert result.architecture

    print("System information tool test passed.")
    print(f"OS: {result.operating_system}")
    print(f"Architecture: {result.architecture}")


if __name__ == "__main__":
    test_system_info()