
a = []

starti = 0
n = 0

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
symbols = {'^': 0, '>': 1, 'v': 2, '<': 3}

with open('/Users/mihnea/Projects/AoC/day6/input.txt', 'r') as file:
    for line in file:
        line = list(line)
        n += 1
        for i in range(len(line)):
            if (line[i] in '^><v'):
                starti = n-1
                startj = i
        a.append(line)

m = len(a[0])
print(a[starti][startj])
visited = [[False for j in range(m)] for i in range(n)]

intialDir = symbols[a[starti][startj]]

ci = starti
cj = startj
cd = intialDir

sol = 0

def isValid (i, j):
    return (i >= 0 and i < n and j >= 0 and j < m)

while(isValid(ci, cj)):
    if not visited[ci][cj]:
        visited[ci][cj] = True
        sol += 1
    ni = ci + directions[cd][0]
    nj = cj + directions[cd][1]

    if not isValid(ni, nj):
        break

    if a[ni][nj] != '#':
        ci = ni
        cj = nj
    else:
        cd += 1
        cd %= 4

print(sol)