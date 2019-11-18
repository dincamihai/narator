# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='narator',
    packages=['narator'],
    scripts=['narator/narator'],
    version='0.1',
    description='Generate markdown work-reports from the body of github issues.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Mihai Dincă',
    author_email='dincamihai@gmail.com',
    license='MIT',
    include_package_data=True,
    package_data={
        'narator': ['templates/*']
    },
    install_requires=[
        "jinja2",
        "requests"
    ],
    tests_requires=[
        'pytest',
    ],
    zip_safe=False
)
