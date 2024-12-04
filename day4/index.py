directions = [[[0, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 0], [1, 0], [2, 0], [3, 0]],
              [[0, 0], [0,-1], [0,-2], [0,-3]],
              [[0, 0], [-1,0], [-2,0], [-3,0]],
              [[0, 0], [1, 1], [2, 2], [3, 3]],
              [[0, 0], [1,-1], [2,-2], [3,-3]],
              [[0, 0], [-1,1], [-2,2], [-3,3]],
              [[0, 0], [-1,-1], [-2,-2], [-3,-3]]
              ]

array = []
sol = 0

def isValid(i, j):
    return (i >= 0 and i < n and j >= 0 and j < m)

with open('/Users/mihnea/Projects/AoC/day4/input.txt', 'r') as file:
    array = [ list(line) for line in file]

for i in range(len(array)-1):
    array[i]=array[i][:-1]

n = len(array)
m = len(array[0])

for i in range(n):
    for j in range(m):
        for d in directions:
            ok = True
            for letter in range(len(d)):
                newi = i + d[letter][0]
                newj = j + d[letter][1]

                if (not ok):
                    break

                if (isValid(newi, newj)):
                    if (letter == 0):
                        if (array[newi][newj] != 'X'):
                            ok = False
                    if (letter == 1):
                        if (array[newi][newj] != 'M'):
                            ok = False
                    if (letter == 2):
                        if (array[newi][newj] != 'A'):
                            ok = False
                    if (letter == 3):
                        if (array[newi][newj] != 'S'):
                            ok = False

                    if (ok == True and letter == 3):
                        sol += 1

print(sol)


# Second part
directions = [[[-1,-1], [1, 1]],
              [[-1, 1], [1,-1]]]

sol = 0

for i in range(n):
    for j in range(m):
        if (array[i][j] == 'A'):
            ok = True
            for d in directions:
                i1 = i + d[0][0]
                i2 = i + d[1][0]
                
                j1 = j + d[0][1]
                j2 = j + d[1][1]

                if (isValid(i1, j1) and isValid(i2, j2)):
                    if ( not( (array[i1][j1] == 'M' and array[i2][j2] == 'S')
                     or (array[i1][j1] == 'S' and array[i2][j2] == 'M') ) ):
                        ok = False
                else:
                    ok = False
            
            if (ok):
                sol += 1

print(sol)