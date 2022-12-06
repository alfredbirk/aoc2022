from utils import *

g = parse_input()
r = 0

for i in range(len(g)):
    s = set(g[i:i+14])
    if len(s) == 14:
        r = i+14
        break

print(r)
pyperclip.copy(r)