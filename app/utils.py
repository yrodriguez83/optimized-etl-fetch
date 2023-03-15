import hashlib


def mask_ip(ip: str) -> str:
    return hashlib.md5(ip.encode()).hexdigest()


def mask_device_id(device_id: str) -> str:
    return hashlib.md5(device_id.encode()).hexdigest()


def mask_data(data: dict) -> dict:
    masked_data = {
        "user_id": data.get("user_id"),
        "app_version": int(data.get("app_version").replace(".", "")),
        "device_type": data.get("device_type"),
        "masked_ip": mask_ip(data.get("ip")),
        "locale": data.get("locale"),
        "masked_device_id": mask_device_id(data.get("device_id")),
        "create_date": datetime.now().strftime("%Y-%m-%d")
    }
    return masked_data
