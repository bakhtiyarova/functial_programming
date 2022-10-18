def check(l):
      a=list()
      for j in range(len(l)):
            a.append(l[j])
      print(a)
      l.sort()
      for i in l:
        if l.index(i)==a.index(i):
            bo=True
        else:
            bo=False
      return bo
l=list()
while True:
  n=int(input())
  if n==0: break
  l.append(n)
if check(l):
  print("List is sorted: ")
else:
  print("List is not sorted: ")