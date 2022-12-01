from utils import *

g = parse_input()
r = 0

m = 0

for line in g:
    c = 0
    for i in line:
        c += int(i)
    m = max(c, m)

r = m
        

print(r)
pyperclip.copy(r)