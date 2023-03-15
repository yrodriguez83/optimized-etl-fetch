import json
from app.sqs import read_messages_from_sqs
from app.postgres import insert_to_postgres
from app.masking import mask_pii


def process_messages(messages):
    processed_records = []

    # Iterate through each message
    for message in messages:
        # Parse the JSON data from the message body
        data = json.loads(message["Body"])
        # Mask the IP and device_id fields
        masked_ip = mask_pii(data["ip"])
        masked_device_id = mask_pii(data["device_id"])

        # Create a tuple with the processed record data
        record = (
            data["user_id"],
            data["device_type"],
            masked_ip,
            masked_device_id,
            data["locale"],
            data["app_version"],
            data["create_date"]
        )
        # Append the processed record to the list of records
        processed_records.append(record)

    return processed_records


def main():
    # Read messages from the SQS Queue
    messages = read_messages_from_sqs()
    # Process the messages to extract and mask the necessary data
    records = process_messages(messages)
    # Insert the processed records into the Postgres database
    insert_to_postgres(records)


if __name__ == "__main__":
    main()
