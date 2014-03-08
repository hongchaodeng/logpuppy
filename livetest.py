#!/usr/bin/env python

import time
import random

readFrom = open('test/access.log')
writeTo = open('test/test.log', 'a')

lines = readFrom.readlines()

for line in lines:
    for _ in xrange(random.randint(1, 10)):
        writeTo.write(line)
        writeTo.flush()
    time.sleep(1)
