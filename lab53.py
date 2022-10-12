l=list()
while True:
    n=int(input())
    if n==0: break
    l.append(n)
l.sort()
print("Sorted list:")
for i in l:
    print(i)