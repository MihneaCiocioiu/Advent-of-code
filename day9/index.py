str = ''
n = 0

with open('/Users/mihnea/Projects/AoC/day9/input.txt', 'r') as file:
    for line in file:
        str = list(line)

for num in str:
    n += int(num)

arr = [-1 for i in range(n)]

ok = True
start = 0
index = 0

for nums in str:
    num = int(nums)
    if ok:
        for i in range(start, start+num):
            arr[i] = index
        index += 1

    ok = not ok
    start += num

right = n - 1
left = 0

while left < right:
    while right >= 0 and arr[right] == -1:
        right -= 1
    while left < n and arr[left] != -1:
        left += 1
    if left < right and arr[left] == -1 and arr[right] != -1:
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp

sol = 0

for i in range(n):
    num = arr[i]
    if num == -1:
        break
    
    sol += num * i

print(sol)