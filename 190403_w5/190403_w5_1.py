def main():
    print('first operand is 0')

def add(a,b):
    global c 
    c = a+b
def sub(a,b):
    global c
    c = a-b

def mul(a,b):
    global c
    c = a*b

def div(a,b):
    global c
    c = a/b

c = 0
operator = 0
main()
while operator != 'exit':
    operator = input('operator (+,-,*,/,exit)\n')
        
    if operator == '+':
         print('operand:')
         operand = float(input())
         add(c, operand)
         print ('result :'+str(c))
         operand = 0
            
    elif operator == '-':
         print('operand:')
         operand = float(input())
         sub(c , operand)
         print ('result :'+str(c))
         operand = 0
             
    elif operator == '*':
         print('operand:')
         operand = float(input())
         mul(c , operand)
         print ('result :'+str(c))
         operand = 0
             
    elif operator == '/':
         print('operand:')
         operand = float(input())
         div(c , operand)
         print ('result :'+str(c))
         operand = 0
             
    elif operator == 'exit':
         print('Program Terminated')
         
    else:
        print('Wrong Input!')
        print ('result : '+str(c))

         
   
    
    