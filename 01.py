from collections import Counter

with open("data/01.txt", "r") as f:
    lines = [list(map(int, l.strip().split('   '))) for l in f.readlines()]

# Part 1
s1, s2 = sorted([i[0] for i in lines]), sorted([i[1] for i in lines])
distance = sum([abs(i1 - i2) for i1, i2 in zip(s1, s2)])

# Part 2
similarity = 0
s2_counter = Counter(s2)
for i in s1:
    similarity += i * s2_counter[i]

print(similarity)