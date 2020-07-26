from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3
from aws_cdk import aws_events
from aws_cdk import aws_events_targets
from aws_cdk import aws_apigatewayv2, aws_apigateway
from aws_cdk import aws_iam


class NewApp(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        myBucket = aws_s3.Bucket(self,
                                 "S3Bucket",
                                 bucket_name="new-app-bucket-example"
                                 )

        myScheduledLambda = _lambda.Function(
            self,
            "scheduled_lambda",
            description="Lambda that will be called according to a schedule",
            function_name="scheduledLambda",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="scheduled_lambda.handler",
            code=_lambda.Code.from_asset("../functions"),
            memory_size=128,  # Memory in mb
            retry_attempts=2,
            environment={"S3_BUCKET": myBucket.bucket_name}
        )

        myBucket.grant_read(myScheduledLambda)
        myBucket.grant_put(myScheduledLambda)

        myScheduledLambdaEvent = aws_events.Rule(
            self,
            "scheduled_lambda_event",
            schedule=aws_events.Schedule.rate(core.Duration.minutes(2)),
            enabled=True,
            targets=[aws_events_targets.LambdaFunction(handler=myScheduledLambda)]
        )

        myEndpointLambda = _lambda.Function(
            self,
            "endpoint_lambda",
            description="Lambda Proxy with Api Gateway",
            function_name="endpointLambda",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="endpoint_lambda.handler",
            code=_lambda.Code.from_asset("../functions"),
            memory_size=128,  # Memory in mb
            retry_attempts=2,
            environment={"S3_BUCKET": myBucket.bucket_name}
        )

        myBucket.grant_read(myEndpointLambda)
        myBucket.grant_put(myEndpointLambda)

        api = aws_apigateway.RestApi(self, "ApiEndpoint")
        api.root.resource_for_path("/test").add_method("GET",
                                                       aws_apigateway.LambdaIntegration(handler=myEndpointLambda))


