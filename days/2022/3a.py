from utils import *

g = parse_input()
r = 0

w = ''
for line in g:
    a,b = line[:len(line)//2], line[len(line)//2:]
    q = ''
    for c in a:
        if c in b:
            q = c
    w += q

for i in w:
    if i.islower():
        r += ord(i) - 96
    else:
        r += ord(i) - 65 + 27

r = w


print(r)
pyperclip.copy(r)