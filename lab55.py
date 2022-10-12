import random
loto=list()
for i in range(0,6):
    s=random.randint(1,49)
    loto.append(s)
    if loto.count(s)>1:
        s=random.randint(1,49)
        loto.append(s)
loto.sort()
print(loto)