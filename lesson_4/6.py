from itertools import count
from itertools import cycle

i = 3
for el in count(i):
    if el >= 10:
        break
    else:
        print(el)

n = 0
param = "FILM"
for el in cycle(param):
    if n > 12:
        break
    else:
        print(el)
        n += 1
