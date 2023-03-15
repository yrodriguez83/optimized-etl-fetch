import json
from datetime import datetime

from app.config import POSTGRES_CONNECTION
from app.postgres import insert_to_postgres
from app.mask_pii import mask_pii_fields
from app.sqs import read_messages_from_sqs
from app.utils import mask_data

def process_messages(messages):
    records = []
    for message in messages:
        data = json.loads(message["Body"])
        masked_data = mask_pii_fields(data)
        record = (
            masked_data["user_id"],
            masked_data["device_type"],
            masked_data["masked_ip"],
            masked_data["masked_device_id"],
            masked_data["locale"],
            masked_data["app_version"],
            masked_data["create_date"],
        )
        records.append(record)
    return records


def main():
    messages = read_messages_from_sqs()
    records = process_messages(messages)
    insert_to_postgres(POSTGRES_CONNECTION, records)


if __name__ == "__main__":
    main()
