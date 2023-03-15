import psycopg2
from psycopg2 import OperationalError
from app.config import POSTGRES_CONNECTION_STRING


def insert_to_postgres(records: list) -> None:
    try:
        # Connect to the Postgres database
        with psycopg2.connect(POSTGRES_CONNECTION_STRING) as conn:
            # Open a new cursor
            with conn.cursor() as cur:
                # Define the SQL query for inserting records
                insert_query = """
                INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                # Execute the bulk insert operation
                cur.executemany(insert_query, records)
                # Commit the changes to the database
                conn.commit()
    # Handle any errors while inserting records into the Postgres database
    except OperationalError as e:
        print(f"Error inserting records into Postgres: {e}")
