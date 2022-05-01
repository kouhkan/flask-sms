"""Flask-sms Installation."""

from setuptools import setup, find_packages

setup(
    name="Flask-SMS",
    version="0.1.0",
    install_requires=["Flask>=2", "kavenegar>=1"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
