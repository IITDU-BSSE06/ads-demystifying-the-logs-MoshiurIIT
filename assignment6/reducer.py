#!/usr/bin/python
import sys
dict = {}
year1=2009
year2 = 2010
year3=2011
count1=0
count2=0
count3=0
for line in sys.stdin:
	path = line.strip()
	dict[path] = dict.get(path, 0) + 1
	for dict[path] in year1
		hitted_path = (dict, key=dict.get)
		count1+=1
	for dict[path] in year2
		hitted_path = (dict, key=dict.get)
		count2+=1
	for dict[path] in year3
		hitted_path = (dict, key=dict.get)
		count3+=1
print "hitted file path in 2009 :"+str(count1)
print "hitted file path in 2010 :"+str(count2)
print "hitted file path in 2011 :"+str(count3)
