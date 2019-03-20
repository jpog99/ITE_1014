import random,time


print('******START*******')

numQues = 0

while numQues < 3:
     a = random.randint(0,9)
     b = random.randint(0,9)
     c = random.randint(0,9)
     d = random.randint(0,9)
     ans = a*b+c-d
     print(str(a) +'*'+ str(b) + '+' + str(c) + '-' + str(d) + '=?')
     for i in range(1,4):
         time.sleep(1)
         print (i, end = ',', flush=True)
     print(':',end='')
         
         
         

     e = input()

     if int(e) == ans:
        print('Correct')
     else:
        print('Wrong! The answer is:' + str(ans))
    
     numQues  = numQues + 1
     print()


