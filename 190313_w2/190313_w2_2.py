

row = 0
while(row < 6):
    row += 1
    spaces = 6 - row
    i = 0
    while(i < spaces):
        print(" ", end='')
        i += 1
        j = 2*row-1
    while(j > 0):
        print("*", end='')
        j -= 1
        
    print ()
