fname = input("Enter file name: ")
fh = open(fname)
str = fh.read()
wrd = str.split()
wrd.sort()

final = []
for i in wrd:
    if i not in final:
        final.append(i)

print(final)










#lst = list(fh)
#for wrd in lst:
#    wrds = wrd.split()
#    print(wrds)
#    #print(lines.split())

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list(fh)
#for wrd in lst:
#    lst = fh.strip()
#    slst = lst.sort()
#print(slst) 





#stock problem

#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print(line.rstrip())
