from setuptools import setup, find_packages

setup(
    name="pymt5linux",
    version="1.0.0",
    author="Henrique Perez de Andrade",
    author_email="hpdeandrade@gmail.com",
    description="MetaTrader5 for Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hpdeandrade/pymt5linux",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    install_requires=[
        "rpyc"
    ]
)