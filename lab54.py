l=list()
while True:
    n=int(input())
    if n==0: break
    l.append(n)
l.sort()
print("Sorted list:")
for i in range(len(l)-1,-1,-1):
    print(l[i])