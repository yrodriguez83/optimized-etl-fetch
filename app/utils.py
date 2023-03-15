import hashlib
from typing import Dict, Any


def mask_ip(ip: str) -> str:
    return hashlib.md5(ip.encode()).hexdigest()


def mask_device_id(device_id: str) -> str:
    return hashlib.md5(device_id.encode()).hexdigest()


def mask_data(data: Dict[str, Any]) -> Dict[str, Any]:
    masked_data = {
        "user_id": data["user_id"],
        "app_version": data["app_version"],
        "device_type": data["device_type"],
        "masked_ip": mask_ip(data["ip"]),
        "locale": data["locale"],
        "masked_device_id": mask_device_id(data["device_id"]),
        # Added this line to include the create_date field
        "create_date": datetime.utcnow().date()
    }
    return masked_data
