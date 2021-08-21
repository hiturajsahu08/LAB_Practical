# Python code to
# demonstrate readlines()

import pandas as pd
import xlrd
from collections import OrderedDict
import json

L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
 
# Using readlines()
file1 = open('candriver.txt', 'r')
Lines = file1.readlines()

Key=['']*100
Value=['']*100
 
#count = 0
i=0
j=0
# Strips the newline character
for line in Lines:
    #count += 1
    #print("Line{}: {}".format(count, line.strip()))
    #print(line)
    if(line.find('>') != -1):
        #Key[i+1] = str(line)
        #Key[i+1]=Key[i+1].replace(">", "")
        #Key[i+1]=Key[i+1].replace("\n", "")
        str_line= str(line)
#        print(str_line)
        str_line=str_line.replace(">", "")
        str_line=str_line.replace("\n", "")
 #       print(str_line)
        Key[i+1] = str_line
        i=i+1
        j=j+1
    #else:(line.find('\n') != -1):.
    else:
        Value[j]=Value[j] + ' ' + line
        Value[j]=Value[j].replace("\n", "")
print(Key)
#print(Value)
#print(Value)
dictionary = dict(zip(Key, Value))
#print(dictionary)
thisdict=dictionary
#for x in thisdict:
#  print(thisdict[x])


df = pd.DataFrame(thisdict.items(),columns=['Date', 'DateValue'])

#df = (df.T)

#print (df)

df.to_excel('dict1.xlsx')
