from utils import *

g = parse_input()
r = 0

for line in g:
    a,b,c,d = parse_positive_nums(line)
    q = list(range(a,b+1))
    w = list(range(c,d+1))
    if set(q) & set(w):
        r += 1

print(r)
pyperclip.copy(r)