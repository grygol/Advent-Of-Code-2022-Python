file = open("input_1_1.txt", "r")
# print(file.read())

all = []
sum = 0
for line in file.readlines():
    if line == '\n':
        all.append(sum)
        sum = 0
    else:
        sum += int(line)

all.sort(reverse=True)
result = all[0] + all[1] + all[2]
print(result)