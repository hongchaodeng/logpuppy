#!/usr/bin/env python

import time
import random

readFrom = open('test/access.log')
writeTo = open('test/test.log', 'w')

lines = readFrom.readlines()

for line in lines:
    for _ in xrange(random.randint(0, 10)):
        writeTo.write(line)
    time.sleep(1)
