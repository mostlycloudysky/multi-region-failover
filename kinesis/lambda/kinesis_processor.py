import json
import base64


def lambda_handler(event, context):
    for record in event["Records"]:
        payload = base64.b64decode(record["kinesis"]["data"])
        print(f"Received record: {payload}")

    return {
        "statusCode": 200,
        "body": json.dumps("Processed records successfully"),
    }
