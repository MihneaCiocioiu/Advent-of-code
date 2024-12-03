import re

sol = 0

enabled = True
newLine = ""

with open('/Users/mihnea/Projects/AoC/day3/input.txt', 'r') as file:
    for line in file:

        dos = []
        donts = []

        for do in re.finditer(r'do\(\)', line):
            dos.append(do.start())

        for dont in re.finditer(r'don\'t\(\)', line):
            donts.append(dont.start())

        # print (dos)
        # print (donts)
        

        for i in range(len(line)):
            if (i in dos):
                enabled = True
            if (i in donts):
                enabled = False
            if (enabled):
                newLine += line[i]

        # if (len(donts) == 0):
        #     newLine = line
        # else:
        #     newLine += line[:donts[0]]
        #     j = 0
        #     lasti = 0
        #     checked = 0
        #     for i in range(len(dos)):
        #         while (j < len(donts) and donts[j] < dos[i]):
        #             j += 1
        #         if (j < len(donts) and i > checked):
        #             newLine += line[dos[i]:donts[j]]
        #             lasti = i+1
        #             checked = max(dos[i], donts[j])
            
        #     if (lasti < len(dos)):
        #         newLine += line[dos[lasti]:]

    patterns = re.findall(r'mul\(\d+,\d+\)', newLine)

    for pattern in patterns:
        pattern = pattern[4:]
        split = pattern.split(',')
        num1 = int(split[0])
        num2 = int(split[1][:-1])

        sol += num1 * num2

print(sol)