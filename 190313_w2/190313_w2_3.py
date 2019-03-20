a = 0
b = 0
while a < 4:
    print(" " * a, end="")
    a += 1
    while b < a:
        print("*" *(9-(2 *b)))
        b+=1

i = 0
j = 0
while i < 5:
    print(" " * (4-i), end="")
    i += 1
    while j < i:
        print("*" *(2 * j + 1))
        j+=1

