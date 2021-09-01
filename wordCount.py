userinput = input('Put the text which you want to be scanned: ')
userinput = userinput.lower()
userinput = userinput.split()
word = input('Which word do you want scanned: ')
word = word.lower()
word_count = 0
for i in userinput:
  if i == str(word):
    word_count+=1
  else:
    word_count+=0
print (word_count)

