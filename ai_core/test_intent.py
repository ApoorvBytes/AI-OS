from ai_core.intent import IntentParser


def test_system_information_intent():
    parser = IntentParser()

    intent = parser.parse("Show me my system information")

    assert intent.name == "get_system_info"
    assert intent.confidence == 1.0


def test_system_info_variation():
    parser = IntentParser()

    intent = parser.parse("Can you show my PC specs?")

    assert intent.name == "get_system_info"


def test_unknown_intent():
    parser = IntentParser()

    intent = parser.parse("Make me a cup of coffee")

    assert intent.name == "unknown"
    assert intent.confidence == 0.0


if __name__ == "__main__":
    test_system_information_intent()
    test_system_info_variation()
    test_unknown_intent()

    print("Intent parser tests passed.")