#!/usr/bin/python
import sys
dic1 = {}
dic2 = {}
for line in sys.stdin:
	path1 = line.strip()
	dic1[path1] = dic1.get(path1, 0) + 1
	path2 = line.strip()
	dic2[path2] = dic2.get(path2, 0) +1


get_req = (dic1, key=dic1.get)
post_req = (dic2, key=dic2.get)
print "GET : "+str(dic1[get_req])+" times"
print "POST : "+str(dic2[get_req])+" times"
