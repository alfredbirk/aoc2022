from utils import *

g = parse_input()
r = 0

for i in range(len(g)):
    s = set(g[i:i+4])
    if len(s) == 4:
        r = i+4
        break

print(r)
pyperclip.copy(r)