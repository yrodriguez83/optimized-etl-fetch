import os

# Define the SQS Queue URL
SQS_QUEUE_URL = os.environ.get(
    "SQS_QUEUE_URL", "http://localhost:4566/000000000000/login-queue")

# Define the Postgres connection string
POSTGRES_CONNECTION_STRING = os.environ.get(
    "POSTGRES_CONNECTION_STRING", "dbname=postgres user=postgres password=postgres host=localhost port=5432")
