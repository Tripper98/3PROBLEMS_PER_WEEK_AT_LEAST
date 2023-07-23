# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import find_packages, setup


setup(
    name='leetcode',
    version='0.1.0',
    description='3 Problems per week',
    author='DRIOUCHE Adnane',
    packages=find_packages(exclude=('tests', 'docs')),
)
