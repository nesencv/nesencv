import os
import re
from setuptools import setup, find_packages, find_namespace_packages
from nesencv.utils import load_module

_version = load_module("./nesencv/__init__.py").__version__

packages = find_packages(
    where=".",
    exclude=(),
    include=("nesen*")
)

setup(
    name="nesencv",
    version=_version,
    description="mini cv",
    author="PancrasChen",
    url="https://www.chenbangguo.com",

    # https://setuptools.pypa.io/en/latest/userguide/dependency_management.html?highlight=entry_points
    entry_points={
        "console_scripts": [
            "nesencv.hello = nesencv.scripts.hello:hello",
            "nesencv.new_pyenv = nesencv.scripts.new_pyenv:new_pyenv",
        ]
    },
    packages=packages,

)

# print(packages)

# python3 setup.py bdist_wheel
# python3 setup.py develop
