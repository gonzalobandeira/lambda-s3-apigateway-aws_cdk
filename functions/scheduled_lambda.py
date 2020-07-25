import json
import boto3
from datetime import datetime
import os


def handler(event, context):
    # Code to be computed goes here

    data = {"time": str(datetime.now())}

    s3 = boto3.resource('s3')
    object = s3.Object(os.environ["S3_BUCKET"], 'test.json').put(Body=json.dumps(data))

    return "file saved"
