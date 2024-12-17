a = []
positions = {}
sol = 0

def isValid(i, j):
    return i >= 0 and i < n and j >= 0 and j < m

with open('/Users/mihnea/Projects/AoC/day8/input.txt', 'r') as file:
    for line in file:
        if line != '\n':
            line = line[:-1]
            a.append(list(line))

n = len(a)
m = len(a[0])

for i in range(n):
    for j in range(m):
        if a[i][j] != '.':
            if a[i][j] not in positions:
                positions[a[i][j]] = []

            positions[a[i][j]].append((i, j))

seen = [[] for i in range(n)]
for i in range(n):
    seen[i] = [False for j in range(m)]

for character in positions:
    poss = positions[character]
    for i in range(len(poss)):
        for j in range(i+1, len(poss)):
            i1 = poss[i][0]
            j1 = poss[i][1]
            i2 = poss[j][0]
            j2 = poss[j][1]
            
            difi = i2-i1
            difj = j2-j1
            
            ni = i2 + difi
            nj = j2 + difj

            if isValid(ni, nj):
                if seen[ni][nj] == False:
                    seen[ni][nj] = True
                    a[ni][nj] = '#'
                    sol += 1
                    # print(f'({ni}, {nj})')

            ni = i1 - difi
            nj = j1 - difj

            if isValid(ni, nj):
                if seen[ni][nj] == False:
                    seen[ni] [nj] = True
                    a[ni][nj] = '#'
                    sol += 1
                    # print(f'({ni}, {nj})')

for line in a:
    str = ''
    for character in line:
        str += character

    print(str)

print(sol)