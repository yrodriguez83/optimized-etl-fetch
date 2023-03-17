# Data Engineering Project
# ETL off an SQS Queue


This project focuses on creating an ETL (Extract, Transform, Load) pipeline to read JSON data containing user login behavior from an AWS SQS Queue, mask specific fields containing personal identifiable information (PII), and writes the transformed data to a PostgreSQL database.

## Project Setup

### Requirements

- Python 3.8+
- Docker
- Docker Compose
- pip
- AWS CLI (for local testing)

### Installation
Step-by-step instructions are as follows:

1. Clone the repository.

2. Install the required Python packages using `pip`:
    ```
    pip install -r requirements.txt
    ```

3. Set up the local development environment using Docker Compose: 
    ```
    docker-compose up -d
    ```

4. Test local access:

- Read a message from the queue using `awslocal`:

  ```
  awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
  ```

- Connect to the PostgreSQL database and verify the table is created:

  ```
  psql -d postgres -U postgres -p 5432 -h localhost -W
  ```

  Then, run the following SQL command:

  ```
  SELECT * FROM user_logins;
  ```

## Project Structure

The project is structured as follows:

- `app/`: The main application folder containing the source code for the ETL pipeline.
- `__init__.py`: Initializes the application package.
- `config.py`: Configuration file containing environment-specific settings.
- `main.py`: The main script responsible for executing the ETL pipeline.
- `masking.py`: Module responsible for masking PII data.
- `postgres.py`: Module responsible for connecting to the PostgreSQL database and inserting records.
- `sqs.py`: Module responsible for reading messages from the SQS Queue.
- `tests/`: Folder containing unit tests for the application modules.
- `docker-compose.yml`: Docker Compose configuration file to set up the local development environment.
- `requirements.txt`: File containing the required Python packages for the project.

## :runner: Running the ETL Pipeline: 

To run the ETL pipeline, execute the following command from the root of the project directory: 
```
python -m app.main
```
This command will read messages from the SQS Queue, process the messages to extract and mask the necessary data, and insert the records into the PostgreSQL database.

## :pray: Running Unit Tests

To run the unit tests, execute the following command from the root of the project directory:
```
pytest tests/
```
This command will run all tests located in the `tests/` folder and display the results.

## :eyes: Assumptions: 

1. The SQS Queue contains JSON data with a consistent structure, containing fields like `user_id`, `device_type`, `ip`, `device_id`, `locale`, `app_version`, and `create_date`.
2. The PII data (IP and device_id) can be masked using a one-way hashing algorithm (e.g., SHA-256) to preserve uniqueness while ensuring that the original data cannot be easily recovered.
3. The PostgreSQL database is set up with the correct table schema to store the processed records.
4. The provided Docker Compose file sets up the local development environment, and no additional configuration is required for local testing.
5. The ETL pipeline is designed to be executed as a standalone script and does not include advanced features like scheduling or error handling.

## :runner:Next Steps: 

1. Add error handling and retries for reading from SQS and writing to PostgreSQL.
2. Implement logging and monitoring to track the application's performance and detect issues.
3. Develop a scheduling mechanism or run the ETL pipeline as a service to process new data periodically.
4. Optimize the data processing, for example, by processing messages in batches to improve performance.
5. Implement more comprehensive tests, including integration and end-to-end tests.

### :raising_hand: Deployment in Production: 

To deploy this application in production, we could use a managed container orchestration service like AWS Fargate or Kubernetes -- it would allow us to easily manage, scale, and monitor the application in a production environment.:grin:

### :speech_balloon: Production-Ready Components:

In order to make this application production-ready, we could add the following components:

1. Centralized logging with services like AWS CloudWatch or ELK Stack (Elasticsearch, Logstash, Kibana) for easy log management and analysis.
2. Monitoring and alerting with tools like Grafana, Prometheus, or Datadog to track the performance and health of the application.
3. CI/CD pipeline for automated building, testing, and deployment of the application.

### :muscle: Scaling with a Growing Dataset:

Finally, to scale this application with a growing dataset, we could take the following approaches depending on our dev environment:

1. Implement ---> horizontal scaling by adding more instances of the ETL application, allowing it to process data concurrently.
2. Optimize database performance with proper indexing, partitioning, and sharding strategies.
3. Use a message broker like Apache Kafka or Amazon Kinesis to handle high throughput and enable data streaming.


