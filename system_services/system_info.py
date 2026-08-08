import platform
import socket
from dataclasses import dataclass


@dataclass
class SystemInfo:
    """Basic information about the host system."""

    operating_system: str
    hostname: str
    architecture: str
    processor: str


class SystemInfoTool:
    """Read basic system information."""

    name = "get_system_info"
    risk_level = "LOW"

    def execute(self) -> SystemInfo:
        return SystemInfo(
            operating_system=platform.system(),
            hostname=socket.gethostname(),
            architecture=platform.machine(),
            processor=platform.processor(),
        )