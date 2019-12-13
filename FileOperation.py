# Reads a given input file and creates a list containing list of words and the number of times used.

f = open("TESTINPUTS.txt")
str=f.read()
print("----------------------------------------------------------------------------------")
print(" Original Text")
print("----------------------------------------------------------------------------------")
print(str)
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
strList = str.split()
strDict ={}
for words in strList:
    chkWord = strDict.get(words, None)
    if (chkWord == None):
        strDict[words] = 1
    else:
        temp = chkWord
        temp += 1
        strDict[words] = temp
f.close()
print("----------------------------------------------------------------------------------")
print(" The result")
print("----------------------------------------------------------------------------------")
print("      Word  -  Count")
print("      --------------")
for keys in sorted(strDict):
    print("%10s  -  %d" % (keys,strDict.get(keys)))
print('----------------------------------------------------------------------------------')