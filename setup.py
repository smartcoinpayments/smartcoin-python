# -*- coding: utf-8 -*-
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'smartcoin'))
from version import __version__

setup(
    name='smartcoin',
    version=__version__,
    author='Felipe Tomaz',
    author_email='felipe@felipetomaz.com',
    packages=['smartcoin'],
    scripts=[],
    url='https://git@github.com/smartcoinpayments/smartcoin-python',
    license='MIT',
    description='The Smartcoin provides a Python REST APIs to create, process and manage payments.',
    long_description="""
      The Smartcoin provides a Python REST APIs to create, process and manage payments.

      https://smartcoin.com.br/api/ - API Reference
    """,
    install_requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['smartcoin', 'smartcoinpayments', 'rest', 'payment'],
    test_suite='smartcoin.test.all',
)
