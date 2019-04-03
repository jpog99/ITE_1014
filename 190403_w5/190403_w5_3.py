import random

num_list = []

for i in range (0,50):
    a = int(random.randint(1,1000))
    num_list.append(a)
print(num_list)
print()
print('Total generated number: ' + str(len(num_list)))
print('Maximum value: '+ str(max(num_list)))
print('Minimum value: '+ str(min(num_list)))


def sort_func():
    inc_list = []
    while num_list:
        min = num_list[0]
        for i in num_list:
            if i < min:
                min = i
        
        inc_list.append(min)
        num_list.remove(min)
    print(inc_list)
    
print('\nList in increasing sequence: ', end = '')
sort_func()