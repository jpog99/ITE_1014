
f = open('article.txt', 'r')
text = f.read()

#removing all punctuation and numbers
punctu = ['.','?','/',':',' ',',','-',"\'",'\"','','[',']','\\','\n','0','1','2','3','4','5','6','7','8','9']
for char in (punctu):
    text = text.replace(char,'')
text.split()


#appending all letters into a list of list
data = {}
for letter in text:
    data[letter] = data.get(letter, 0) +1
    
list = list(data.items())


#appending letter which is not found in text and set its value to 0
keys=[]
for k in range (len(list)):
    keys.append(list[k][0])
    
for idx in range (ord('A'), ord('Z')+1):
    if chr(idx) not in keys:
        a = [chr(idx), 0]
        a = tuple(a)
        list.append(a)


#sorting the list in alphabetical order
def sort_alpha():
    unsorted = True
    while unsorted:
        unsorted = False             
        for idx in range(0,len(list)-1):
            if list[idx] > list[idx + 1]:
                swap = list[idx + 1]
                list[idx + 1] = list[idx]
                list[idx] = swap
                unsorted = True      
    sortedList = list
    for i in range (len(sortedList)):
        print(sortedList[i][0], ':' , sortedList[i][1])

#sorting the list in numerical order
def sort_num():
    list2 = list
            
    for max in range(len(list2)-1, -1, -1):
        change = False
        for i in range(max):
            if list2[i][1] > list2[i+1][1]: #just change between > and < for different order
                list2[i], list2[i+1] = list2[i+1], list2[i]
                change= True
        if not change:
            break
        
    for i in range (len(list2)):
        print(list2[i][0], ':' , list2[i][1])
        

print('ALPHABETICAL ORDER')
sort_alpha()
print('\nNUMERICAL ORDER')
sort_num()


    
