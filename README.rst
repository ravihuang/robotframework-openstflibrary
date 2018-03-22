
.. image:: https://secure.travis-ci.org/ravihuang/robotframework-openstflibrary.png?branch=master
  :target: http://travis-ci.org/ravihuang/robotframework-openstflibrary

robotframework-openstflibrary
--------------------------

**robotframework-stublibrary** is a `Robot Framework
<https://github.com/robotframework/robotframework>`_ test library for openstf
needs. It uses `pyswagger <https://pypi.python.org/pypi/pyswagger>`_ library
underneath now.

Installation
------------

You can install robotframework-openstflibrary via `pip
<http://www.pip-installer.org/>`_::

  pip install --upgrade robotframework-openstflibrary

Usage
-----
API documentation can be found at
`https://github.com/ravihuang/robotframework-openstflibrary
<https://github.com/ravihuang/robotframework-openstflibrary/>`_, here is an example
on how to use it:

============  ================
  Setting          Value      
============  ================
Library       OpenstfLibrary
============  ================

\

============  =================================  ===================================
 Test Case    Action                             Argument
============  =================================  ===================================
Example
              Connect To Stf    192.168.117.155:7100    8ad3024193ba44a1820afef3060df8934d964599b74049d4b11b9c3f9edb5457
              ${x}              Get Idle Device
============  =================================  ===================================


Compatibility
-------------
This library is only tested on CPython. It might work on Jython, not sure.

Development
-----------
If you want to hack on this library itself, this should get you started::

  # install
  git clone https://github.com/peritus/robotframework-openstflibrary.git
  cd robotframework-openstflibrary/
  python setup.py install
    
  # run tests
  pybot tests/

I'm very happy about patches, pull-requests and API-discussions (as this is
mostly a wrapper supposed to have a nice API)!

Changelog
---------

**v0.1.0**

- new

License
-------
Apache License

