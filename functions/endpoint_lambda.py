import boto3
import os


def handler(event, context):
    # Code to be used goes here
    print(event)
    if event["httpMethod"] == "GET" and event["path"] == "/test":
        s3 = boto3.client('s3')
        body = s3.get_object(Bucket=os.environ["S3_BUCKET"], Key='test.json')["Body"].read()
        body = body.decode('utf8').replace("'", '"')
        return {"statusCode": 200, "body": body}
    else:
        return {"statusCode": 500, "body": "Method not supported"}


if __name__ == "__main__":
    print(handler({}, object))
