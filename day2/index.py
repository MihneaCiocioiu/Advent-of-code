sol = 0

def checkLine(list):
        increasing = True
        decreasing = True
        valid      = True
        problems   = 0
        for i in range(len(list)-1):
            ok = True
            if (list[i] < list[i+1]):
                decreasing = False
            else:
                increasing = False
            if (abs(list[i]-list[i+1]) <1 or abs(list[i]-list[i+1]) > 3):
                valid = False

        if (valid and (increasing or decreasing)):
            return True

with open('/Users/mihnea/Projects/AoC/day2/input.txt', 'r') as file:
    for line in file:
        list = []
        for num in map(int, line.split()):
            list.append(num)
        
        if (checkLine(list)):
            sol += 1

print(sol)

# Second part

sol = 0

with open('/Users/mihnea/Projects/AoC/day2/input.txt', 'r') as file:
    for line in file:
        list = []
        for num in map(int, line.split()):
            list.append(num)
        
        if (checkLine(list)):
            sol += 1
            continue

        for i in range(len(list)):
            newList = []
            newList += list[:i]
            newList += list[i+1:]

            if (checkLine(newList)):
                sol += 1
                break

print(sol)