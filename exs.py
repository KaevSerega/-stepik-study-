n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
g, q1, q2, q3, q4 = 1, 0, 0, 0, 0

while True:
    for i in range(0+q1, 1+q1):
        for j in range(0+q1, n-1-q1):
            a[i][j] = g
            g += 1
            if g > n*n: break
        q1 += 1
    if g > n * n: break

    for j in range(n-1-q2, n-q2):
        for i in range(0+q2, n-q2):
            a[i][j] = g
            g += 1
            if g > n * n: break
        q2 += 1
    if g > n * n: break

    for i in range(n-1-q3, n-q3):
        for j in range(n-2-q3, 0+q3,-1):
            a[i][j] = g
            g += 1
            if g > n * n: break
        q3 += 1
    if g > n * n: break

    for j in range(0+q4, 1+q4):
        for i in range(n-1-q4, 0+q4, -1):
            a[i][j] = g
            g += 1
            if g > n * n: break
        q4 += 1
    if g > n * n: break

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
