file = open("input_1_1.txt", "r")
# print(file.read())

max = -1
sum = 0
for line in file.readlines():
    if line == '\n':
        if sum > max:
             max = sum
        sum = 0
    else:
        sum += int(line)

print(max)