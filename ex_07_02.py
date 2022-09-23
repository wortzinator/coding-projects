# Use the file name mbox-short.txt as the file name
 
fname = input("Enter file name: ")

total = 0
count = 0
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):        
        continue
    else :
        count = count +1
        l = len(line)
        #l is for length of line
        p = line.find(str(0))
        #p is for position in the line 
    
    lp = (line[p:l])
    lf = float(lp)
    total = total + lf
    average = total/count

print('Average spam confidence:',average)   
