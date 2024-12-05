import re


with open("data/03.txt", "r") as f:
    lines = f.readlines()


# Part 1
pattern = r"mul\((\d*),(\d*)\)"
s = 0
for line in lines:
    for match in re.findall(pattern, line):
        s += int(match[0]) * int(match[1])

print(s)


# Part 2
s = 0
pattern_dos = r"do\(\)(.*?)don't\(\)"
for line in lines:
    line = "do()" + line + "don't()"
    for part in re.findall(pattern_dos, line, re.DOTALL):
        for match in re.findall(pattern, part):
            s += int(match[0]) * int(match[1])

print(s)