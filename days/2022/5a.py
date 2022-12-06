from utils import *

g = parse_input()

q = [
["J","F","C","N","D","B","W"],
["T","S","L","Q","V","Z","P"],
["T","J","G","B","Z","P"],
["C","H","B","Z","J","L","T","D"],
["S","J","B","V","G"],
["Q","S","P"],
["N","P","M","L","F","D","V","B"],
["R","L","D","B","F","M","S","P"],
["R","T","D","V"],
]


for i in range(len(q)):
    q[i] = q[i][::-1]


for line in g:
    num, frm, to = parse_positive_nums(line)
    w = []
    for _ in range(num):
        q[to-1].append(q[frm-1].pop())

r = ''

for i in q:
    if i:
        r += i[-1]


print(r)
pyperclip.copy(r)