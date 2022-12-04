from utils import *

g = parse_input()
r = 0

for line in g:
    a,b,c,d = parse_positive_nums(line)
    if a >= c and b <= d or c >= a and d <= b:
        r += 1

print(r)
pyperclip.copy(r)