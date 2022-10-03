from re import T
from xmlrpc.client import TRANSPORT_ERROR


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d1 = dict()
count = 0

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        time = line.split()[5]
        hh = time.split(':')[0]
    else:
        continue
    if hh not in d1:
        d1[hh] = 1
    else:
        d1[hh] += 1

lst = list()
for key, val in list(d1.items()):
    lst.append((key, val))
    lst.sort(reverse=False)
            
for key, val in lst[:10]:
    print(key, val)


#10.2 Write a program to read through the mbox-short.txt 
#and figure out the distribution by hour of the day for 
#each of the messages. You can pull the hour out from the 
#'From ' line by finding the time and then splitting the 
#string a second time using a colon. 
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.


#name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
#handle = open(name)


#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1