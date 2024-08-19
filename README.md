# Multi-Region AWS Kinesis Streams Failover Simulation

## Overview
This project demonstrates how to simulate a failover scenario for AWS Kinesis and Firehose using LocalStack. The setup involves:

- Creating Kinesis streams and Firehose delivery streams.
- Deploying a Lambda function to process Kinesis data.
- Simulating a failover by switching data streams between regions.

```
multi-region-failover/
│
├── kinesis/
│   ├── lambda/
│   │   └── kinesis_processor.py  # Lambda function to process Kinesis data
│   │
│   ├── scripts/
│   │   ├── create_kinesis_streams.py  # Script to create Kinesis streams
│   │   ├── create_lambda_function.py  # Script to create the Lambda function
│   │   ├── create_firehose_streams.py  # Script to create Firehose delivery streams
│   │   └── simulate_failover.py  # Script to simulate region failover
│   │
│   ├── tests/
│   │   └── test_kinesis_failover.py  # Unit test for failover simulation
├── docker-compose.yml  # Docker Compose file to run LocalStack
├── requirements.txt  # Python dependencies
├── README.md  # Project documentation
└── .gitignore  # Git ignore file
```

## Prerequisites
- `Python 3.9+`
- `LocalStack`: Local AWS service emulator.
- `Docker`: To run LocalStack.
- `AWS CLI`: For interacting with LocalStack.

## Setup Instructions

1. Create and Activate a Virtual Environment
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
2. Start LocalStack using Docker Compose:
   ```sh
   docker-compose up -d
   ```
   Ensure LocalStack is running on `http://localhost:4566`.
3. Install AWS CLI and Boto3
   ```sh
   pip install awscli boto3
   ```
4. Configure AWS CLI for LocalStack:
   ```sh
   aws configure --profile localstack
   ```
   ```sh
   AWS Access Key ID: test
   AWS Secret Access Key: test
   Default region name: us-east-1
   Default output format: json
   ```
5. Use the profile with LocalStack by setting an environment variable:
   ```sh
   export AWS_PROFILE=localstack
   export AWS_DEFAULT_REGION=us-east-1
   ```

## Create resources with LocalStack
Run the following scripts to set up Kinesis streams, Firehose delivery streams, and the Lambda function:
```sh
python kinesis/scripts/create_kinesis_streams.py
python kinesis/scripts/create_firehose_streams.py
python kinesis/scripts/create_lambda_function.py
```

These scripts will:
- Create the primary and secondary Kinesis streams.
- Create the Firehose delivery streams.
- Deploy the Lambda function to process Kinesis data.

## Running the Failover Simulation

1. Run the Simulation Script:
   Execute the failover simulation script:
   ```sh
   python kinesis/scripts/simulate_failover.py
   ```
   This script will:

   - Send data to the primary Kinesis stream.
   - Simulate a failover by deleting the primary stream.
   - Wait for a short period to simulate downtime.
   - Send data to the secondary Kinesis stream. 

2. Verify Results:
   Check the script output to confirm whether data was successfully redirected to the secondary Kinesis stream after the primary stream was deleted.

## Running Tests
1. Run Tests
   Execute the tests to verify the functionality of the failover simulation script:
   ```sh
   python -m unittest discover kinesis/tests/
   ```
