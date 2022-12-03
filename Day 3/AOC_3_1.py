file = open('input_3.txt')
result = 0

for line in file.readlines():
    middle = len(line)//2
    leftCompartment = set(line[0:middle])
    rightCompartment = set(line[middle:len(line)])
    # print(leftCompartment + " : " + rightCompartment)
    for c in leftCompartment:
        if c in rightCompartment:
            num = ord(c)
            # print(c + " (" + str(num) + ")")
            if 97 <= num <= 122:
                num -= 96
            elif 65 <= num <= 90:
                num -= 38
            result += num
            break
print(result)
