import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from app.config import POSTGRES_CONNECTION
from app.postgres import insert_to_postgres
from app.sqs import read_messages_from_sqs
from app.mask_pii import mask_pii_data
from datetime import datetime

# Define a dataclass for storing the processed record information
@dataclass
class Record:
    user_id: str
    device_type: str
    masked_ip: str
    masked_device_id: str
    locale: str
    app_version: str
    create_date: str

# Create a Record object from the masked data dictionary
def create_record(masked_data: Dict[str, Any]) -> Optional[Record]:
    if masked_data is None:
        return None

    # Convert the app version to an integer by removing the dots
    app_version = int(masked_data["app_version"].replace(".", ""))

    # Return a Record object with the masked data and converted app version
    return Record(
        user_id=masked_data["user_id"],
        device_type=masked_data["device_type"],
        masked_ip=masked_data["masked_ip"],
        masked_device_id=masked_data["masked_device_id"],
        locale=masked_data["locale"],
        app_version=app_version,
        create_date=masked_data["create_date"],
    )

# Process the messages read from the SQS queue
def process_messages(messages: List[Dict[str, Any]]) -> List[Record]:
    records = []

    # Iterate through each message and extract the data
    for message in messages:
        data = json.loads(message["Body"])
        print(f"Loaded message data: {data}")
        # Mask the PII data in the message
        masked_data = mask_pii_data(data)
        # Create a Record object from the masked data
        record = create_record(masked_data)

        if record is not None:
            records.append(record)

    return records

# Main function for running the ETL process
def main():
    # Read messages from the SQS queue
    messages = read_messages_from_sqs()
    print(f"Messages: {messages}")

    # Process the messages and create a list of Record objects
    records = process_messages(messages)
    print(f"Records: {records}")

    # Insert the records into the PostgreSQL database
    insert_to_postgres(POSTGRES_CONNECTION, records)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
