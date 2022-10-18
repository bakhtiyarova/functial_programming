def check(l):
    a=l
    l=l.sort()
    if a==l:
        return True
    return False
l=list()
while True:
    n=int(input())
    if n==0: break
    l.append(n)
if check(l):
    print("List is sorted")
else:
    print("List isn't sorted")