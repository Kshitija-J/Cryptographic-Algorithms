import string
import re

with open('ciphertext','r') as file:
    Ciphertext_Str = file.read();
cipherList=[]
decList=[]

cipherList=[x for x in Ciphertext_Str]
print(cipherList)

def hextodecimal(str):
        i=0
        while i<len(cipherList):
           str=cipherList[i]+cipherList[i+1]
           print("\n")
           print(str)
           res=int(str,16)
           decList.append(res)
           str=""
           i=i+2
        return decList

BinaryList=[]
i=0
y=[]
def decTobinary(x):
        if x >= 1:
         decTobinary(x//2)
         value=x % 2
         #print(value)
         y.append(value)

key="133457799BBCDFF1"

key1=hextodecimal(key)
keybin=decTobinary(key1)

print("Key: ", keybin)

n=0
while n<len(decList):
        decTobinary(decList[n])
        n=n+1

print(y)
print(len(y))
print(decList)









