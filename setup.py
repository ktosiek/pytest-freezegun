#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-freezegun',
    version='0.1.0',
    author='Tomasz Kontusz',
    author_email='tomasz.kontusz@gmail.com',
    maintainer='Tomasz Kontusz',
    maintainer_email='tomasz.kontusz@gmail.com',
    license='MIT',
    url='https://github.com/ktosiek/pytest-freezegun',
    description='Wrap tests with fixtures in freeze_time',
    long_description=read('README.rst'),
    py_modules=['pytest_freezegun'],
    install_requires=[
        'freezegun>0.3',
        'pytest>=3.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'freezegun = pytest_freezegun',
        ],
    },
)
