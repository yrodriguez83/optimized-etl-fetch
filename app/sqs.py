import boto3
from botocore.exceptions import ClientError
from app.config import SQS_QUEUE_URL

# Initialize SQS client with the local endpoint
sqs = boto3.client("sqs", endpoint_url="http://localhost:4566")


def read_messages_from_sqs(max_messages: int = 10) -> list:
    messages = []
    try:
        # Receive messages from the SQS Queue in batches
        response = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=max_messages
        )
        # Check if there are any messages in the response
        if "Messages" in response:
            messages = response["Messages"]
            # Delete each message from the queue after reading it
            for message in messages:
                sqs.delete_message(
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=message["ReceiptHandle"]
                )
    # Handle any errors while reading messages from the SQS Queue
    except ClientError as e:
        print(f"Error reading messages from SQS: {e}")

    return messages
