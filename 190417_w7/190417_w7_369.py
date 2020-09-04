n = int(input('Please insert the limit interger\n'))

for i in range(n+1):
    clapcount = 0
    i = str(i)
    for digit in i:
        if digit in '369':
            clapcount += 1
    if clapcount == 0:
        print (i)
    else:
        print ('clap' * clapcount)

"""
number = 19
string_number = str(number) "19"

string_number[0] # 1
string_number[1] # 9

if (x == 3,6,9?

"""