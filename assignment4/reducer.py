#!/usr/bin/python
import sys
dic = {}
for line in sys.stdin:
	path = line.strip()
	dic[path] = dic.get(path, 0) + 1

popular_hitted_path = max(dic, key=dic.get)
print "most popular file was hitted: "+str(dic[popular_hitted_path])+" times"
