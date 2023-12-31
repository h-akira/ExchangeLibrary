#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-12-30 03:41:28

from setuptools import setup, find_packages
with open("requirements.txt", "r") as f:
  install_requires = f.read().splitlines()
setup(name='ExchangeLibrary',version='1.0.3', install_requires=install_requires, packages=find_packages())
