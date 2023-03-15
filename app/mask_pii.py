import hashlib


def mask_pii_fields(data):
    masked_data = data.copy()
    masked_data["masked_ip"] = hashlib.sha256(data["ip"].encode()).hexdigest()
    masked_data["masked_device_id"] = hashlib.sha256(
        data["device_id"].encode()).hexdigest()
    del masked_data["ip"]
    del masked_data["device_id"]
    return masked_data
