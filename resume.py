class Resume:
    first_name=""
    last_name=""
    email=""
    birth_date=""
    skills=""
    link_to_git=""
    def __init__(self,first_name,last_name,email,birth_date,skills,link_to_git):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.birth_date=birth_date
        self.skills=skills
        self.link_to_git=link_to_git
    def printResume(self):
        print("_______________RESUME_______________")
        print("First name: "+first_name)
        print("____________________________________")
        print("Last name: "+last_name)
        print("____________________________________")
        print("Email: "+email)
        print("____________________________________")
        print("Birth date: "+birth_date)
        print("____________________________________")
        print("Skills: "+skills)
        print("____________________________________")
        print("Link to github: "+link_to_git)
        print("____________________________________")
l=list()
k=0
while k<1:
    for i in range(1):
        print("Enter your fisrt name:")
        first_name=input()
        print("Enter your last name:")
        last_name=input()
        print("Enter your email:")
        email=input()
        print("Enter your birth_date:")
        birth_date=input()
        print("Enter your skills:")
        skills=input()
        print("Enter your link to github:")
        link_to_git=input()
        person=Resume(first_name,last_name,email,birth_date,skills,link_to_git)
    l.append(person)
    k+=1
for j in range(len(l)):
    l[j].printResume()
