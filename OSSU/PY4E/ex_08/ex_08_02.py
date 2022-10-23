count = 0

fname = input("Enter file name: ")
hname = open(fname)
#sline = hname.read()
#lin = hname.split()
for line in hname:
    line = line.rstrip()
    if line.startswith('From '):
        print(line.split()[1])
        count = count + 1
    if not line.startswith('From ') :
        continue


#print(line)..


#print("There were", count, "lines in the file with From as the first word")
#
#
#
#    if line.startswith('From '):
#        for word in line:
#            counts[line] = counts.get(line, 0) + 1
#    if not line.startswith('From '):
#        continue#
#
#bigcount = None
#bigword = None
#for word, count in counts.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count#

#print(bigword, bigcount)