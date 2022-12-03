from utils import *

g = parse_input()
r = 0

w = ''
for a,b,c in chunks(g,3):
    q = set([i for i in a if i in b and i in c])
    for i in q:
        w += i


for i in w:
    if i.islower():
        r += ord(i) - 96
    else:
        r += ord(i) - 65 + 27

print(r)
pyperclip.copy(r)