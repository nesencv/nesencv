#!/usr/bin/env python3


import os
import argparse

parser = argparse.ArgumentParser(
    description="demo for setup.py scripts",
)


def hello():
    args = parser.parse_args()
    print("hello scripts.")


if __name__ == '__main__':
    hello()
