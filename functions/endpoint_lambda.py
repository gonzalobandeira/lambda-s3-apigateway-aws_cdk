import boto3
import os


def handler(event, context):
    # Code to be computed goes here
    s3 = boto3.client('s3')
    body = s3.get_object(Bucket=os.environ["S3_BUCKET"], Key='test.json')["Body"].read()
    body = body.decode('utf8').replace("'", '"')
    return {"statusCode": 200, "body": body}


if __name__ == "__main__":
    print(handler({}, object))
