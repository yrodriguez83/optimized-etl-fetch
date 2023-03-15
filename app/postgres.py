import psycopg2
from psycopg2.extras import execute_values


def convert_records_to_tuples(records):
    tuple_list = []
    for record in records:
        
        print(f"Record: {record.__dict__}")
        tuple_list.append((record.user_id, record.device_type, record.masked_ip,
                          record.masked_device_id, record.locale, record.app_version, record.create_date))
    return tuple_list


def insert_to_postgres(connection_params, records):
    insert_query = """
    INSERT INTO user_logins (
        user_id,
        device_type,
        masked_ip,
        masked_device_id,
        locale,
        app_version,
        create_date
    ) VALUES %s;
"""

    with psycopg2.connect(**connection_params) as conn:
        with conn.cursor() as cur:
            # Convert the Record objects to tuples
            converted_records = convert_records_to_tuples(records)

            print(f"Inserting records: {converted_records}")
            execute_values(cur, insert_query, converted_records)
        conn.commit()
