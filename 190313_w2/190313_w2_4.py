import time

start = time.time()

for i in range(0, 200):
    print('*', end = '')

end = time.time()

print(end - start)

start1 = time.time()

s = ''
for g in range(0, 200):
    s += '*'
print(s)
end1 = time.time()

print(end1 - start1)
