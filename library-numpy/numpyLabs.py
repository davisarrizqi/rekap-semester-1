import numpy
import os
import time

# declare some variables
numberMemory = []; numberLength = 0
codeMemory = []; isDone = False



# notes for our phase
print("[ Length-Input Phase ]")

# insert the length of our number
numberLength = int(input("how much number will going on? --> "))

# make sure the numberLength is not an odd
while numberLength %2!=0:
    print("this is an odd number, please insert the even number")
    numberLength = int(input("how much number will going on? --> "))



print(" ") # --> blank space

# notes for our phase
print("[ Element-Input Phase ]")

# make a for-loop so that we can insert it's variable
for loopCount in range(numberLength):
    insertNumber = int(input(f"apppend for {loopCount} index --> "))
    numberMemory.append(insertNumber)



print(" ") # --> blank space

# notes for our phase
print("[ Array-Processing Phase ]")

# change it into an numpy array
numberMemory = numpy.array(numberMemory)
print(numberMemory)



print(" ") # --> blank space

# notes for our phase
print("[ Change-Dimension Phase ]   --+--   [ once-said format ]  [ default ]")

# select your own format
myFormat = input("select your input-format: ")

# once-said format
if(myFormat == "once-said format"):
    myFormat = input("input your code: ")    
    try: myRow = int(myFormat[0]); myColumn = int(myFormat[2]); isDone = True
    except: pass

# default format
else:
    myRow = int(input("your matrix's row ordo: "))
    myColumn = int(input("yout matrix's column ordo: "))
    isDone = True

# avoid bugs that caused by failed on once-said format
if(isDone == False):
    myRow = int(input("your matrix's row ordo: "))
    myColumn = int(input("yout matrix's column ordo: "))
    isDone = True
else: pass

# debug our result
print("\n Before Transpose ")
numberMemory = numberMemory.reshape(myRow, myColumn)
print(numberMemory)


print("\n After Transpose")
numberMemory = numberMemory.transpose()
print(numberMemory)
