def drawline(n):
    star = "*"
    space = ' '
    endline = ''

    for i in range (0,n):
    
        for j in range(i, n):
            print(star, end='')
        for j in range (0, 2 * i):
            print(space, end='')
        for j in range(i,n):
            print(star, end='')
        print(endline)

    for i in range(0, n-1):
        for j in range(0, i + 2):
            print(star,end='')
        for j in range(0, 2*(n-1-i) - 2):
            print(space,end='')
        for j in range(0, i+2):
            print(star,end='')

        print(endline)

lvl = int(input('Height of diamond: '))
drawline(lvl) 