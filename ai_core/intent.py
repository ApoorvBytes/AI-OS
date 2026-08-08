from dataclasses import dataclass


@dataclass(frozen=True)
class Intent:
    """Represents the user's requested action."""

    name: str
    confidence: float


class IntentParser:
    """Simple deterministic intent parser for the AI OS prototype."""

    def parse(self, text: str) -> Intent:
        normalized = text.lower().strip()

        system_info_phrases = [
            "system information",
            "system info",
            "computer information",
            "computer specs",
            "pc information",
            "pc specs",
            "show my system",
            "show system information",
            "tell me my system information",
        ]

        if any(phrase in normalized for phrase in system_info_phrases):
            return Intent(
                name="get_system_info",
                confidence=1.0,
            )

        return Intent(
            name="unknown",
            confidence=0.0,
        )