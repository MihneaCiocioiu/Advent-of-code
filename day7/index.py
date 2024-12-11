sol = 0

with open('/Users/mihnea/Projects/AoC/day7/input.txt', 'r') as file:
    for line in file:
        line = line.split(' ')
        target = int(line[0][:-1])
        # print(target)

        line[0] = line[0][:-1]
        for i in range(len(line)):
            line[i] = int(line[i])

        tree = [0 for i in range(2**len(line))]
        level = [0 for i in range(2**len(line))]

        tree[1] = line[1]
        level[1] = 1

        for i in range(1, 2**len(line)-1):
            level[i] = level[int(i/2)] + 1
            if level[i] < len(line) - 1:
                tree[i*2] = tree[i] * line[level[i]+1]
                tree[i*2+1] = tree[i] + line[level[i]+1]


        for i in range(2**(len(line)-2), 2**(len(line)-1)):
            if tree[i] == target:
                sol += target
                break

print(sol)