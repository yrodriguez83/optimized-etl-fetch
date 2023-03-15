import hashlib
from typing import List, Dict, Any, Optional
from datetime import datetime

# Function to mask PII data in the input dictionary
def mask_pii_data(data: Dict[str, Any]) -> Dict[str, Any]:
    # Extract values from the input data
    user_id = data.get("user_id")
    device_type = data.get("device_type")
    ip = data.get("ip")
    device_id = data.get("device_id", "unknown")
    locale = data.get("locale", "unknown")
    app_version = data.get("app_version")

    print(f"Raw data: {data}")

    # Check for required fields in the input data
    if user_id is None or device_type is None or ip is None or app_version is None:
        print(f"Invalid data: {data}")
        return None

    # Mask the IP and device_id using SHA-256 hashing
    masked_ip = hashlib.sha256(ip.encode("utf-8")).hexdigest()
    masked_device_id = hashlib.sha256(device_id.encode("utf-8")).hexdigest()

    # Create a dictionary with the masked data
    masked_data = {
        "user_id": user_id,
        "device_type": device_type,
        "masked_ip": masked_ip,
        "masked_device_id": masked_device_id,
        "locale": locale,
        "app_version": app_version,
    }

    print(f"Masked data: {masked_data}")

    # Return the masked data dictionary along with the current timestamp as create_date
    return {
        "user_id": user_id,
        "device_type": device_type,
        "masked_ip": masked_ip,
        "masked_device_id": masked_device_id,
        "locale": locale,
        "app_version": app_version,
        "create_date": datetime.now(),
    }
