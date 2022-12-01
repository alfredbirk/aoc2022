from utils import *

g = parse_input()
r = 0

m = 0

a = []

for line in g:
    c = 0
    for i in line:
        c += int(i)
    a.append(c)

a.sort()

r = sum(a[-3:])
        

print(r)
pyperclip.copy(r)