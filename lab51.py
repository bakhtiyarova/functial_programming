from audioop import reverse

def check(l,newl):
    bo=True
    for i in range(len(l)):
        if l[i]==newl[i]:
            bo=False
    return bo
l=list()
for i in range(5):
    print("Enter number:")
    n=int(input())
    l.append(n)
a=l
print(a)
l.sort()
b=check(a,l)
if b==True: print("List is sorted")
else: print("List is not sorted")


