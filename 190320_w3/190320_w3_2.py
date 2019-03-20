import random

print('******START*******')

numQues = 0

while numQues < 3:
     a = random.randint(0,9)
     b = random.randint(0,9)
     ans = a*b
     print(str(a) +'*'+ str(b) + ':?')
     
     c = input()

     if int(c) == ans:
        print('Correct')
     else:
        print('Wrong')
    
     numQues  = numQues + 1
     print()


