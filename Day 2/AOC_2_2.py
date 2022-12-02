file = open("input_2_1.txt", "r")

sum = 0

for line in file.readlines():
    roundResult = 0
    if line[2] == 'X':
        if line[0] == 'A':
            roundResult += 3
        elif line[0] == 'B':
            roundResult += 1
        elif line[0] == 'C':
            roundResult += 2
    elif line[2] == 'Y':
        roundResult += 3
        if line[0] == 'A':
            roundResult += 1
        elif line[0] == 'B':
            roundResult += 2
        elif line[0] == 'C':
            roundResult += 3
    elif line[2] == 'Z':
        roundResult += 6
        if line[0] == 'A':
            roundResult += 2
        elif line[0] == 'B':
            roundResult += 3
        elif line[0] == 'C':
            roundResult += 1
    sum += roundResult

print(sum)