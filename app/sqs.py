from app.config import SQS_QUEUE_URL
from botocore.exceptions import ClientError
import boto3
import os

os.environ["AWS_ACCESS_KEY_ID"] = "dummy_access_key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "dummy_secret_key"


# Initialize SQS client with the local endpoint and a region
sqs = boto3.client("sqs", endpoint_url="http://localhost:4566",
                   region_name="us-east-1")


def read_messages_from_sqs(max_messages: int = 10) -> list:
    messages = []
    try:
        response = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=max_messages
        )
        if "Messages" in response:
            messages = response["Messages"]
            for message in messages:
                sqs.delete_message(
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=message["ReceiptHandle"]
                )
    except ClientError as e:
        print(f"Error reading messages from SQS: {e}")

    return messages
