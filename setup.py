#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='crimg',
    version='0.0.1',
    description='Crop and resize an image without aspect ratio distortion.',
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/crimg',
    entry_points={
        'console_scripts': [
            'crimg = crimg.bin:main',
        ],
    },
    install_requires=['Pillow'],
    packages=find_packages(exclude=("tests", "tests.*")),
)
