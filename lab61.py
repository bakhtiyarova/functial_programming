class Address:
    street="Valihanova"
    no_house=82
    def get_address(self):
        return "Street: "+self.street+"\n№ "+str(self.no_house)
    def get_street(self):
        return self.street
    def get_No(self):
        return self.no_house

class Skills:
    skills=list()
    def get_Skill(self):
        return self.skills
    def get_Skills(self):
        skills=""
        for i in range(len(self.skills)):
            skills+=self.skills[i]+" "
        return "Skills: "+skills+"\n"
    def set_skill(self,skill):
        if self.skills:
            self.skills.append(skill)
        else:
            self.skills.append(skill)
    def remove_skill(self,skill):
        if skill in self.skills:
            self.skills.remove(skill)
class Person:
    first_name="Akbala"
    last_name="Bakhtiyarova"
    birth_date="27/02/2002"
    age=20
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_birth_date(self):
        return self.birth_date
    def get_age(self):
        return self.age
    def get_info(self):
        return "Name: "+self.first_name+"\nSirname: "+self.last_name+"\nBirth date: "+self.birth_date+"\nAge: "+str(self.age)+"\n"
class Resume():
    person=Person()
    skills=Skills()
    address=Address()
    def get_resume(self):
        print("RESUME")
        print(self.person.get_info())
        print("______________________________")
        self.skills.set_skill("C/C++")
        self.skills.set_skill("Java")
        self.skills.set_skill("Python")
        print(self.skills.get_Skills())
        print("______________________________")
        print(self.address.get_address())
    def get_person(self):
        return self.person
    def get_skills(self):
        return self.skills
    def get_address(self):
        return self.address
resume=Resume()
resume.get_resume()
akbala=(resume.get_person().first_name,resume.get_person().get_last_name(),resume.get_skills().get_Skill())
employee={}
for i in range(3):
    skill=input()
    employee[i]=skill
for j in range(len(employee)):
    if employee[j] in akbala[2]:
        print("He/She has " + employee[j])
new_skill=set()
new_skill.add("HTML")
resume.get_skills().set_skill(new_skill)
print(akbala)





    





    

