import psycopg2
from psycopg2.extras import execute_values


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
            execute_values(cur, insert_query, records)
        conn.commit()
