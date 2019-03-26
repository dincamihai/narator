# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='narator',
    packages=['narator'],
    version='0.1',
    description='',
    url='',
    author='Mihai Dincă',
    author_email='dincamihai@gmail.com',
    license='MIT',
    include_package_data=True,
    package_data = {
        'narator': ['templates/*']
    }
    install_requires=[
        "jinja2"
    ],
    tests_requires=[
        'pytest',
    ],
    zip_safe=False
)
