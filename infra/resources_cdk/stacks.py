from aws_cdk import core
from aws_cdk import aws_lambda as _lambda


class NewApp(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        myLambda = _lambda.Function(
            self,
            id="test_function",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="function.handler",
            code=_lambda.Code.from_asset("functions")
        )