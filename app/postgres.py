import psycopg2
from psycopg2.extras import execute_values

# Function to convert a list of 'Record' objects to a list of tuples
def convert_records_to_tuples(records):
    tuple_list = []
    for record in records:
        # Print the attributes of the 'Record' object
        print(f"Record: {record.__dict__}")
        # Add the record's attributes as a tuple to the list
        tuple_list.append((record.user_id, record.device_type, record.masked_ip,
                          record.masked_device_id, record.locale, record.app_version, record.create_date))
    return tuple_list

# Function to insert records into the 'user_logins' table in the Postgres database
def insert_to_postgres(connection_params, records):
    # SQL query to insert records into the 'user_logins' table
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

    # Connect to the Postgres database
    with psycopg2.connect(**connection_params) as conn:
        with conn.cursor() as cur:
            # Convert the Record objects to tuples
            converted_records = convert_records_to_tuples(records)

            # Print the records being inserted
            print(f"Inserting records: {converted_records}")
            # Execute the insert query with the records as tuples
            execute_values(cur, insert_query, converted_records)
        # Commit the transaction
        conn.commit()
