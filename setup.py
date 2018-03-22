#!/usr/bin/env python
#coding:utf-8
#  Copyright (c) 2017 Ravi Huang
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Setup script for Robot's OpenstfLibrary distributions"""
import re,os
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'src', 'OpenstfLibrary', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)
with open(join(CURDIR, 'README.rst'),'rb') as f:
    DESCRIPTION = str(f.read())

setup(
    name             = 'robotframework-openstflibrary',
    version          = VERSION,
    description      = 'Openstf utility library for Robot Framework',
    long_description = DESCRIPTION,
    author           = 'Ravi Huang',
    author_email     = 'ravi.huang@gmail.com',
    url              = 'https://github.com/ravihuang/Robotframework-OpenstfLibrary',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation openstf android',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    install_requires = ['robotframework\n','pyswagger'],
    package_dir      = {'': 'src'},
    packages         = find_packages('src')
)
