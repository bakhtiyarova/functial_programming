import random
def Random(n):
    a=list()
    for i in range(n):
        b=random.randint(1,10)
        a.append(b)
    return a
def min(a):
    a.sort()
    return a
n=int(input())
print(Random(n))
print(min(Random(n)))

