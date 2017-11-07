#!/usr/bin/python

import sys

ip_count=0

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) != 1 :
        continue
    
    url = str(data[0])
    if "10.99.99.186" == url:
        ip_count+=1


print "number of hits: "+str(ip_count)
