#!/usr/bin/python
import sys
dict = {}
for line in sys.stdin:
	path = line.strip()
	dict[path] = dict.get(path, 0) + 1
max_hitted_path = max(dict, key=dict.get)
print "maximum hitted file path :"+str(max_hitted_path)
