#!/usr/bin/env python3

import sys
from setuptools import setup

TESTING = any(x in sys.argv for x in ['test', 'pytest'])

README = open("README.rst").read()

CLASSIFIERS = """\
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
""".splitlines()

pytest_asyncio_version = '==0.8' if sys.version_info.minor == 7 else '<0.6'

setup(
    name="aioconsole",
    version="0.1.8.dev0",
    packages=["aioconsole"],
    entry_points={'console_scripts': ['apython = aioconsole:run_apython']},

    setup_requires=['pytest-runner' if TESTING else ''],
    tests_require=['pytest',
                   'pytest-asyncio{}'.format(pytest_asyncio_version),
                   'pytest-cov'],

    license="GPLv3",
    classifiers=CLASSIFIERS,
    description="Asynchronous console and interfaces for asyncio",
    long_description=README,

    author="Vincent Michel",
    author_email="vxgmichel@gmail.com",
    url='https://github.com/vxgmichel/aioconsole',
    download_url='http://pypi.python.org/pypi/aioconsole',
)
