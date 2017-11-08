#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data1 = line.strip().split("GET")
	data2 = line.strip().split("POST")
	if len(data) == 2:
		path1 = urlparse(data[1].split()[0]).path
		path2 = urlparse(data[1].split()[0]).path
		if path1:
			print str(path1)
		if path2:
			print str(path2)
