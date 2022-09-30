name = input("Enter file:")
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
di = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()[1]
        if line in di:
            di[line] = di.get(line,0) + 1
        else:
            di[line] = 1
        #print(line,di[line])
    else:
        continue
#print(di)

bigcount = None
bigword = None
for word,count in di.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)





# Stock Input:
#name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
#handle = open(name)


#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
# number of mail messages. The program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python 
# dictionary that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Desired Output:
# cwen@iupui.edu 5