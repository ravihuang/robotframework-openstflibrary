#!/bin/bash

test -d gh-pages || git clone `git remote show origin|grep Fetch|awk '{print $3}'` gh-pages -b gh-pages
cd src/ && ../bin/libdoc HttpStub ../gh-pages/HttpStub.html
