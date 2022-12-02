from utils import *

g = parse_input()
r = 0


a = ['A','B','C']
b = ['X','Y','Z']
c = [1, 2, 3]
for line in g:
    o, y = line.split()
    y_ind = b.index(y)
    o_ind = a.index(o)
    r += c[y_ind]
    if (y_ind - o_ind) % 3 == 1:
        r += 6

    if (y_ind - o_ind) % 3 == 0:
        r += 3
    
    

print(r)
pyperclip.copy(r)