
def printLine(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):  
            print(num, end=" ") 
           
            num = num + 1
       
        print() 

def printLine2(n):
    for i in range(1, n+1):
        for j in range(1, n - i + 2):
            print(str(j) + " ", end='')

        print()
    
print('enter number: ')
n = int(input())
printLine(n)
printLine2(n)