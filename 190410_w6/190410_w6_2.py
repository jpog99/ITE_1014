from asyncore import read
from dataclasses import replace
f = open('article.txt','r')
text = f.read()

for char in (':.,\'?[]-"/'):
    text = text.replace(char,'')
    
wordlist = text.lower().split()

dict = {}
for word in wordlist:
    dict[word] = dict.get(word, 0) +1

tot = 0
for (key,val) in dict.items():
    print(key,':',val)
    tot += val

print('Total words : '+ str(len(wordlist)))
f.close()