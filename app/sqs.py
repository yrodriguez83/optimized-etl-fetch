from app.config import SQS_QUEUE_URL
from botocore.exceptions import ClientError
import boto3
import os

# Set up environment variables for dummy AWS credentials
os.environ["AWS_ACCESS_KEY_ID"] = "dummy_access_key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "dummy_secret_key"

# Initialize SQS client with the local endpoint and a region
sqs = boto3.client("sqs", endpoint_url="http://localhost:4566",
                   region_name="us-east-1")

# Function to read messages from the SQS queue
def read_messages_from_sqs(max_messages: int = 10) -> list:
    messages = []
    try:
        # Request messages from the SQS queue
        response = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=max_messages
        )
        # Check if the response contains messages
        if "Messages" in response:
            messages = response["Messages"]
            # Delete each message after it's read from the queue
            for message in messages:
                sqs.delete_message(
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=message["ReceiptHandle"]
                )
    except ClientError as e:
        # Print any errors that occur while reading messages from the queue
        print(f"Error reading messages from SQS: {e}")

    return messages
