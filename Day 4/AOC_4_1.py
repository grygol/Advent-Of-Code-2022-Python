file = open("input.txt", "r")

result = 0

for line in file.readlines():
    # pair = line.replace('\n', '').split(',')
    pair = line.replace('\n', '').replace(',', '-').split('-')
    pair = [eval(i) for i in pair]
    if pair[0] >= pair[2] and pair[1] <= pair[3]:
        result += 1
    elif pair[2] >= pair[0] and pair[3] <= pair[1]:
        result += 1
print(result)