file = open("input.txt", "r")

result = 0

for line in file.readlines():
    # pair = line.replace('\n', '').split(',')
    pair = line.replace('\n', '').replace(',', '-').split('-')
    pair = [eval(i) for i in pair]
    if pair[0] >= pair[2] and pair[1] <= pair[3]:
        print(pair)
        result += 1
    elif pair[2] >= pair[0] and pair[3] <= pair[1]:
        print(pair)
        result += 1
    elif pair[0] <= pair[3] and pair[0] >= pair[2]:
            print(pair)
            result += 1
    elif pair[0] <= pair[3] and pair[1] >= pair[3]:
            print(pair)
            result += 1        
    elif pair[1] >= pair[2] and pair[0] <= pair[2]:
            print(pair)
            result += 1        
    elif pair[1] >= pair[2] and pair[1] <= pair[3]:
            print(pair)
            result += 1
print(result)