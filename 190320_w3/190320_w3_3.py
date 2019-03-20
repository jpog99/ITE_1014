import random,time

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
         time.sleep(5)
         print('Wrong! The answer is:' + str(ans))
    
     numQues  = numQues + 1
     print()


