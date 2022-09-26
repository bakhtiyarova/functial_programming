import random
def Random(n):
    a=list()
    for i in range(n):
        b=random.randrange(1,100,2)
        a.append(b)
    return a
def min(a):
    a.sort()
    for id,value in enumerate(a):
        if id==0: break;
    return value
n=random.randint(2,10)
print("n=%i"%n)
a=Random(n)
print(a)
print(min(a))

