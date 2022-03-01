from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="genbid007",
    description="CNN with MLOPS with templating from Sunny",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genbid007-ml/CNN_FSDS",
    author_email="genbid007.ml@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        #"tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas",
        "pyyaml"
    ]
)