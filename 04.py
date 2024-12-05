
with open("data/04.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
pattern = "XMAS"

def data_gen_h():
    yield data
    yield [l[::-1] for l in data]
    data_t = [''.join([d[i] for d in data]) for i in range(len(data[0]))]
    yield data_t
    yield [l[::-1] for l in data_t]

def data_gen_diag():
    yield data
    yield [l[::-1] for l in data]
    data_t = [''.join([d[i] for d in data]) for i in range(len(data[0]))]
    yield [l[::-1] for l in data_t]
    data_t2 = [''.join([d[len(d) - 1 - i] for d in data]) for i in range(len(data[0]))]
    yield [l[::-1] for l in data_t2]


def hz(lines):
    for line in lines:
        for e in range(len(line) - len(pattern) + 1):
            yield line[e: e + len(pattern)]


def diag(lines):
    for e, line in enumerate(lines):
        if e < len(lines) - len(pattern) + 1:
            for e2 in range(len(line) - len(pattern) + 1):
                yield ''.join([lines[e + idx][e2 + idx] for idx in range(len(pattern))])


nb = 0
for d in data_gen_h():
    for p in hz(d):
        if p==pattern:
            nb += 1

for d in data_gen_diag():
    for p in diag(d):
        if p==pattern:
            nb += 1

print(nb)


# Part 2
nb = 0

def validate(p):
    if p[1][1]=='A':
        if (set([p[0][0], p[2][2]])=={'M', 'S'}) and (set([p[0][2], p[2][0]])=={'M', 'S'}):
            return True
    return False


for e1 in range(len(data) - 3 + 1):
    for e2 in range(len(data[0]) - 3 + 1):
        p = [d[e2:e2+3] for d in data[e1:e1+3]]
        if validate(p):
            nb += 1

print(nb)