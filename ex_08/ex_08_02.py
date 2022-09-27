fname = input("Enter file name: ")
text_file = open(fname)#
str = text_file.read()#

testArray = str.split()#

testArray.sort()#
print(testArray)