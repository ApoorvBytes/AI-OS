from dataclasses import dataclass
from typing import Protocol


@dataclass
class AIResponse:
    """Standard response returned by an AI provider."""

    content: str
    model: str
    provider: str


class AIProvider(Protocol):
    """Interface that every AI provider must implement."""

    def generate(self, prompt: str) -> AIResponse:
        ...


class MockProvider:
    """Temporary provider used for development and testing."""

    def generate(self, prompt: str) -> AIResponse:
        return AIResponse(
            content=f"Mock response for: {prompt}",
            model="mock-model",
            provider="mock",
        )