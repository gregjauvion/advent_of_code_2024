import numpy as np

with open("data/02.txt", "r") as f:
    lines = [list(map(int, l.strip().split(' '))) for l in f.readlines()]


# Part 1
def is_safe(l):
    diffs = np.diff(l)
    is_inc_or_dec = ((diffs>0).sum()==len(diffs)) or ((diffs<0).sum()==len(diffs))
    return is_inc_or_dec and ((np.abs(diffs) <= 3).sum() == len(diffs))

print(sum([is_safe(l) for l in lines]))

# Part 2
def is_safe(l):
    for e in range(len(l)):
        diffs = np.diff([l[i] for i in range(len(l)) if i!=e])
        is_inc_or_dec = ((diffs>0).sum()==len(diffs)) or ((diffs<0).sum()==len(diffs))
        if is_inc_or_dec and ((np.abs(diffs) <= 3).sum() == len(diffs)):
            return True
    return False

print(sum([is_safe(l) for l in lines]))