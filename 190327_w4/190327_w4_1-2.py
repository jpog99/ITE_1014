print('Input a number: ')
num=input()
n=1

while (n<int(num)+1): 
    if (n%2!=0)or(n%4==0):
        print(n)
    n+=1