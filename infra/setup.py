import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="Sample endpoint App",
    version="0.0.1",
    description="Sample endpoint App with CDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gonzalo Bandeira",
    package_dir={"": "resources_cdk"},
    python_requires=">=3.6",
)
