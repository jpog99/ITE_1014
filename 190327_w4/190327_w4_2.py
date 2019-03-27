import random

def comp(var1,var2):
    if var1 > var2:
        return 1
    elif var1 < var2:
        return -1
    elif var1 == var2:
        return 0

guess = 'yes'

a = random.randint(0,100)
while guess == 'yes':
    print('Guess:')
    
    b=int(input())
    x = comp(a,b)
    
    if (x == 1):
        print('Bigger than '+ str(b))
    elif(x == -1):
        print('Smaller than '+ str(b))
    elif(x == 0):
        print('Correct')
        break