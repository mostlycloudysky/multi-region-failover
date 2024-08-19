import boto3


ENDPOINT_URL = "http://localhost:4566"


def create_kinesis_stream(stream_name, region_name):
    kinesis = boto3.client(
        "kinesis", region_name=region_name, endpoint_url="http://localhost:4566"
    )
    kinesis.create_stream(StreamName=stream_name, ShardCount=1)
    print(f"Kinesis stream '{stream_name}' created in {region_name}")


if __name__ == "__main__":
    create_kinesis_stream("PrimaryStream", "us-east-1")
    create_kinesis_stream("SecondaryStream", "us-east-2")
