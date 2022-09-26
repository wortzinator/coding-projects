fname = input("Enter file name: ")
fh = open(fname)
lst = list(fh)
for line in lst:
    line = line.strip()
    lines = line.split()
    print(lines)
    #print(lines.split())













#stock problem

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print(line.rstrip())
