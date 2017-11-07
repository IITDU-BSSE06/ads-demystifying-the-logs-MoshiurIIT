#!/usr/bin/python
import sys
uniq_files = set()
for line in sys.stdin:
	path = line.strip()
	uniq_files.add(path)

print "uniq files: "+str(len(uniq_files))
