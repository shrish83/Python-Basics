import re

handle = open("C3-W2-Actual.txt", "r")
intList = list()
Sum = 0
for line in handle:
    list = re.findall("[0-9]+",line)
    intList = intList + list
for i in intList:
    num = int(i)
    Sum = Sum + num
print(Sum)

#Sum = sum(intList)
#print(Sum)