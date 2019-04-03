def spiral_matrix(n):
    num_block = [[0] * n for i in range(n)]
    x_dir, y_dir = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, num = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += x_dir[i % 4]
            y += y_dir[i % 4]
            num_block[x][y] = num
            num += 1
    return num_block #return the sequence as a block of array

n = int(input('Enter a positive number:\n'))
for i in spiral_matrix(n): 
    print(*i)