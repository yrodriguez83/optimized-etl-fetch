import pytest
from app.postgres import insert_to_postgres
from unittest.mock import MagicMock, patch


def test_insert_to_postgres():
    records = [
        ("user_id_1", "device_type_1", "masked_ip_1",
         "masked_device_id_1", "locale_1", 1, "2022-01-01"),
        ("user_id_2", "device_type_2", "masked_ip_2",
         "masked_device_id_2", "locale_2", 2, "2022-01-02")
    ]

    with patch("app.postgres.psycopg2") as mock_psycopg2:
        mock_conn = MagicMock()
        mock_cur = MagicMock()

        # Mock the psycopg2 connection context manager
        mock_psycopg2.connect.return_value.__enter__.return_value = mock_conn
        # Mock the psycopg2 cursor context manager
        mock_conn.cursor.return_value.__enter__.return_value = mock_cur

        # Test if the insert_to_postgres function successfully inserts records
        insert_to_postgres(records)

        # Assert that the psycopg2 connection and cursor are used correctly
        mock_psycopg2.connect.assert_called_once()
        mock_conn.cursor.assert_called_once()

        # Assert that the SQL query for inserting records is executed with the correct data
        mock_cur.executemany.assert_called_once_with("""
                INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, records)
        # Assert that the changes are committed to the database
        mock_conn.commit.assert_called_once()
