def countPriority(num):
    if 97 <= num <= 122:
        num -= 96
    elif 65 <= num <= 90:
        num -= 38
    return num

file = open('input_3.txt')
result = 0

lines = file.readlines()
for i in range(0, len(lines), 3):
    line1 = set(lines[i])
    line2 = set(lines[i+1])
    line3 = set(lines[i+2])
    for c in line1:
        if c in line2 and c in line3 and c != '\n':
            result += countPriority(ord(c))
            break

print(result)