import os
import re
from setuptools import setup, find_packages, find_namespace_packages
from nesencv.utils import load_module

_version = load_module("./nesencv/__init__.py").__version__

packages = find_packages(
    where=".",
    exclude=(),
    include=("nesen*",)
)

setup(
    name="nesencv",
    version=_version,
    description="mini cv",
    anthor="PancrasChen",
    url="https://www.chenbangguo.com",
    packages=packages

)


# python3 setup.py bdist_wheel
# python3 setup.py develop
