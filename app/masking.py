import hashlib


def mask_pii(data: str, method: str = "sha256") -> str:
    # Check the selected masking method
    if method == "sha256":
        # Return the hashed representation of the data using the SHA-256 algorithm
        return hashlib.sha256(data.encode("utf-8")).hexdigest()
    # I could add more masking methods here if deemed necessary for production!
    else:
        # Raise an error if the selected method is not supported
        raise ValueError(f"Invalid masking method: {method}")
