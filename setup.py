#!/usr/bin/env python
import os
import sys

from setuptools.command import build as build_module
from setuptools import setup, find_packages

PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIR, "src"))

from oscar import get_version  # noqa isort:skip





setup(
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    version=get_version(),
)
