#!/usr/bin/env python

import time

readFrom = open('test/access.log')
writeTo = open('test/test.log')

lines = readFrom.readlines()

for line in lines:
    writeTo.write(line)
    time.sleep(1)
