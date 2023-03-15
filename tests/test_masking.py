import pytest
from app.mask_pii import mask_pii


def test_mask_pii_sha256():
    input_data = "example_data"
    expected_output = "ae1d31f8c0bc324ebf384c447d5c1b89be9b9a9e5d507a17e50f2a1e779ca24d"

    # Test if the mask_pii function returns the correct SHA-256 hash for the given input
    assert mask_pii(input_data) == expected_output


def test_mask_pii_invalid_method():
    with pytest.raises(ValueError):
        # Test if the mask_pii function raises a ValueError when an invalid method is provided
        mask_pii("example_data", method="unsupported_method")
