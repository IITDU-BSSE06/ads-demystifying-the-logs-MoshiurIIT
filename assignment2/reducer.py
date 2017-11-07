#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
    path = line.strip()
    if path == "/assets/js/the-associates.js":
        count = count + 1

print "Number of hits were made to path :"+str(count)
