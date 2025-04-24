from setuptools import setup, find_packages

setup(
    name="pymt5linux",
    version="1.0",
    author="Morteza Omidi",
    author_email="Mortezaomidi24@yahoo.com",
    description="MetaTrader5 for Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tradeset/py3mt5linux",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rpyc"
    ]
)