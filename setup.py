import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="DevApp",
    version="2.1",
    description="DevAppProject is a app for generating application maps",
    url="devapp.io",
    python_requires=">=3.8",
    long_description="DevAppProject is a app template for developing",
    long_description_content_type="text/markdown",
    author="Cristiano Oliveira",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["devapp = app.cli:main"]
    }
)
