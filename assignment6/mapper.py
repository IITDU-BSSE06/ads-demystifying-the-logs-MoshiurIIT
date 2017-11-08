#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
    data = line.strip().split("GET")
    if len(data) > 1:
        path = urlparse(data[1].split()[0]).path
        if path:
            print str(path)
