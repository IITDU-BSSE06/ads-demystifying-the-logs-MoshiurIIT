#!/usr/bin/python
import sys
dict = {}
for line in sys.stdin:
	path = line.strip()
	if(path == "http://www.the-associates.co.uk")
		dict[path] = dict.get(path, 0) + 1
max_hitted_path = max(dict, key=dict.get)
print "Filename with relative path :"+str(max_hitted_path)
