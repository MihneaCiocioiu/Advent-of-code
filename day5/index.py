import re

a = {}
for i in range (100):
    a[i] = []

sol = 0

wrongs = []

with open('/Users/mihnea/Projects/AoC/day5/input.txt', 'r') as file:
    for line in file:
        if ('|' in line):
            split = line.split('|')
            num1 = int(split[0])
            num2 = int(split[1])

            a[num1].append(num2)

        elif line != '\n':
            ok = True
            line = line[:-1]
            nums = line.split(',')

            for i in range(len(nums)):
                nums[i] = int(nums[i])

            for i in range(len(nums)):
                for neighbor in a[nums[i]]:
                    if neighbor in nums[:i]:
                        ok = False
            
            if (ok == True):
                sol += nums[int(len(nums)/2)]

            else:
                wrongs.append(nums)

print(sol)

# print(wrongs)

#Part 2
#Topsort yay

sol = 0
def dfs(nums,i):
    global sorted
    global visited

    visited[i] = True

    for neighbor in a[i]:
        if (neighbor in nums):
            if (not visited[neighbor]):
                dfs(nums, neighbor)

    sorted.append(i)

for nums in wrongs:
    global visited
    visited = [False for i in range(100)]

    global sorted
    sorted = []
    for i in range(len(nums)):
        if (not visited[nums[i]]):
            dfs(nums,nums[i])

    sol += sorted[int(len(sorted)/2)]

print(sol)
