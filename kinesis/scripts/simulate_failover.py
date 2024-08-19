import subprocess
import time
import base64


def encode_data(data):
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")


def simulate_failover():
    primary_data = "Test data from primary region"
    secondary_data = "Test data from secondary region"

    # Encode data in base64
    encoded_primary_data = encode_data(primary_data)
    encoded_secondary_data = encode_data(secondary_data)

    print("Sending data to primary region...")
    result = subprocess.run(
        [
            "awslocal",
            "kinesis",
            "put-record",
            "--stream-name",
            "PrimaryStream",
            "--data",
            encoded_primary_data,
            "--partition-key",
            "1",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("Success: Data sent to primary region.")
    else:
        print("Failure: Could not send data to primary region.")
        print("Error Output:", result.stderr)

    # Simulate primary Kinesis stream failure by stopping the primary stream
    print("\nSimulating primary Kinesis stream failure...")
    stop_result = subprocess.run(
        [
            "awslocal",
            "kinesis",
            "delete-stream",
            "--stream-name",
            "PrimaryStream",
        ],
        capture_output=True,
        text=True,
    )
    if stop_result.returncode == 0:
        print("Success: Primary Kinesis stream deleted.")
    else:
        print("Failure: Could not delete primary Kinesis stream.")
        print("Error Output:", stop_result.stderr)

    time.sleep(5)

    # Sending data to the secondary Kinesis stream
    print("\nSending data to secondary region...")
    result = subprocess.run(
        [
            "awslocal",
            "kinesis",
            "put-record",
            "--stream-name",
            "SecondaryStream",
            "--data",
            encoded_secondary_data,
            "--partition-key",
            "1",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("Success: Data sent to secondary region.")
    else:
        print("Failure: Could not send data to secondary region.")
        print("Error Output:", result.stderr)

    # Optionally, recreate the primary Kinesis stream
    print("\nRecreating primary Kinesis stream...")
    recreate_result = subprocess.run(
        [
            "awslocal",
            "kinesis",
            "create-stream",
            "--stream-name",
            "PrimaryStream",
            "--shard-count",
            "1",
        ],
        capture_output=True,
        text=True,
    )
    if recreate_result.returncode == 0:
        print("Success: Primary Kinesis stream recreated.")
    else:
        print("Failure: Could not recreate primary Kinesis stream.")
        print("Error Output:", recreate_result.stderr)


if __name__ == "__main__":
    simulate_failover()
