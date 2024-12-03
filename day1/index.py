list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())  # Split the line and convert to integers
        list1.append(num1)
        list2.append(num2)

list1 = sorted(list1)
list2 = sorted(list2)

sol = 0

for i in range(len(list1)):
    x = list1[i]
    num = 0
    for j in range(len(list2)):
        if (list2[j] == x):
            num += 1
    sol += num * x

print(sol)