import pytest
import json
from app.sqs import read_messages_from_sqs
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_sqs_response():
    return {
        "Messages": [
            {
                "Body": json.dumps({"key": "value"}),
                "ReceiptHandle": "test_receipt_handle"
            }
        ]
    }


def test_read_messages_from_sqs(mock_sqs_response):
    with patch("app.sqs.sqs") as mock_sqs:
        mock_sqs.receive_message.return_value = mock_sqs_response
        mock_sqs.delete_message.return_value = None

        # Test if the read_messages_from_sqs function returns the correct messages from the mock SQS response
        messages = read_messages_from_sqs()
        assert len(messages) == 1
        assert json.loads(messages[0]["Body"]) == {"key": "value"}
