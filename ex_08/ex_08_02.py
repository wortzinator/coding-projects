count = 0

fname = input("Enter file name: ")
hname = open(fname)
#sline = hname.read()
#lin = hname.split()
for line in hname:
    line = line.rstrip()
    if line.startswith('From '):
        print(line)
        count = count + 1
    if not line.startswith('From ') :
        continue


#print(line)


print("There were", count, "lines in the file with From as the first word")
