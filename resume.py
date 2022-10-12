i=0
a=list()
while True:
    if(i==1): break
    print("Enter your fisrt name:")
    first_name=input()
    a.append(first_name)
    print("Enter your last name:")
    last_name=input()
    a.append(last_name)
    print("Enter your email:")
    email=input()
    a.append(email)
    print("Enter your birth_date:")
    date=input()
    a.append(date)
    print("Enter your skills:")
    skills=input()
    a.append(skills)
    i=1
l=["first_name","last_name","email","birth_date","skills"]
for j in range(len(l)):
    print(l[j]+": "+a[j])


    