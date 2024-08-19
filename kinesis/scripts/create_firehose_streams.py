import boto3


def create_firehose_streams(stream_name, kinesis_arn, region):
    firehose = boto3.client(
        "firehose", region_name=region, endpoint_url="http://localhost:4566"
    )
    firehose.create_delivery_stream(
        DeliveryStreamName=stream_name,
        KinesisStreamSourceConfiguration={
            "KinesisStreamARN": kinesis_arn,
            "RoleARN": "arn:aws:iam::000000000000:role/firehose-role",
        },
        S3DestinationConfiguration={
            "RoleARN": "arn:aws:iam::000000000000:role/firehose-role",
            "BucketARN": "arn:aws:s3:::mybucket",
        },
    )
    print(f"Kinesis Firehose '{stream_name}' created in {region}")


if __name__ == "__main__":
    create_firehose_streams(
        "PrimaryDeliveryStream",
        "arn:aws:kinesis:us-east-1:000000000000:stream/PrimaryStream",
        "us-east-1",
    )

    create_firehose_streams(
        "SecondaryDeliveryStream",
        "arn:aws:kinesis:us-west-2:000000000000:stream/SecondaryStream",
        "us-east-2",
    )
