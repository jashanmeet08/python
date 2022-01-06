introString = input("enter String")
characterCount = 0
wordCount = 1
for i in introString: 
    characterCount = characterCount+1
    if (i ==""):
        wordCount = wordCount+1

print("no of words in string")
print(wordCount)
