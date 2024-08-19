import boto3
import zipfile


def create_lambda_function():
    lambda_client = boto3.client("lambda", endpoint_url="http://localhost:4566")

    # Create a ZIP file containing the Lambda code
    with zipfile.ZipFile("function.zip", "w") as z:
        z.write("kinesis/lambda/kinesis_processor.py", arcname="kinesis_processor.py")

    with open("function.zip", "rb") as f:
        zipped_code = f.read()

    lambda_client.create_function(
        FunctionName="KinesisProcessor",
        Runtime="python3.9",
        Role="arn:aws:iam::000000000000:role/lambda-exec-role",
        Handler="kinesis_processor.lambda_handler",
        Code={"ZipFile": zipped_code},
        Timeout=300,
    )
    print("Lambda function 'KinesisProcessor' created.")


if __name__ == "__main__":
    create_lambda_function()
