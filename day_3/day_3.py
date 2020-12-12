import fileinput

condition = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
m = []

lines = fileinput.input()
for line in lines:
    m.append(list(line.strip()))#import each line and split 
ans = 1
for (x, y) in condition:
    r = 0
    c = 0
    tot = 0
    while r < len(m):
        c += x
        r += y
        if r<len(m) and m[r][c%len(m[r])] == '#':
            tot += 1
    ans *= tot
    if x == 3 and y == 1: #print the solution of the first task
        print(tot)
print(ans)
