def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2)) #recursion function here

n = input('Enter the amount of sequence:\n')
n = int(n)

print("Fibonacci sequence:")

i = 0
while i <= n:
    print('Fibonacci(' + str(i) +')= ' + str(fibonacci(i)))
    i += 1