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

    if y == 'Y':
        r += c[o_ind]
        r += 3
    
    if y == 'Z':
        r += c[(o_ind + 1) % 3]
        r += 6

    if y == 'X':
        r += c[(o_ind - 1) % 3]
    
        

    


print(r)
pyperclip.copy(r)