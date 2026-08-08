from model import MockProvider


def test_mock_provider():
    provider = MockProvider()

    response = provider.generate("Hello AI OS")

    assert response.provider == "mock"
    assert response.model == "mock-model"
    assert response.content == "Mock response for: Hello AI OS"


if __name__ == "__main__":
    test_mock_provider()
    print("AI Core test passed.")
    