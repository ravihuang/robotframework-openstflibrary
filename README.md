OpenstfLibrary
=============================
.. contents::

Introduction
------------
robotframework openstf library

Compile
------------
Env:
    pip install wheel twine -i https://pypi.douban.com/simple
dist：
    python setup.py sdist bdist_wheel --universal
upload to pypi:
    twine upload --config-file c:\Users\Administrator\.pypirc dist\*
