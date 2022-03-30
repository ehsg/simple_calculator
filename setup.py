from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="basic_calculator",
    version="0.0.1",
    author="Eduardo Garcia",
    author_email="eduardogarcia2001@gmail.com",
    description="Simple math calc",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehsg/simple_calculator"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)