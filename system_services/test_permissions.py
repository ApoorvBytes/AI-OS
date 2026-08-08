from .permissions import (
    PermissionManager,
    PermissionRequest,
    RiskLevel,
)


def test_low_risk_is_allowed():
    manager = PermissionManager()

    request = PermissionRequest(
        tool_name="get_system_info",
        risk_level=RiskLevel.LOW,
        reason="Read basic system information",
    )

    assert manager.request(request) is True


def test_high_risk_requires_approval():
    manager = PermissionManager()

    request = PermissionRequest(
        tool_name="delete_file",
        risk_level=RiskLevel.HIGH,
        reason="Delete a file",
    )

    assert manager.request(request) is False

    manager.approve("delete_file")

    assert manager.request(request) is True


def test_permission_can_be_revoked():
    manager = PermissionManager()

    manager.approve("delete_file")
    assert manager.is_approved("delete_file") is True

    manager.revoke("delete_file")
    assert manager.is_approved("delete_file") is False


if __name__ == "__main__":
    test_low_risk_is_allowed()
    test_high_risk_requires_approval()
    test_permission_can_be_revoked()

    print("Permission system tests passed.")
    