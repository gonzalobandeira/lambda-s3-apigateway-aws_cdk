#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import Tag

from infra.resources_cdk.stacks import NewApp
from infra.resources_cdk.config import SERVICE, STAGE, AWS_ACCOUNT, REGION

app = core.App()

# To ensure we don't have an environment-agnostic stack we need to add region and
# account as envs: https://github.com/aws/aws-cdk/issues/3083
NewApp(app, "exampleApp", env={"region": REGION, "account": AWS_ACCOUNT})

# Set tags to all the resources
tags = [
    Tag("di:application-name", SERVICE),
    Tag("di:environment-type", STAGE),
]
for tag in tags:
    Tag.add(app, tag.key, tag.value)

app.synth()
