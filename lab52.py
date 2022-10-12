def printAll(name):
    students=["Akbala","Asan","Akzhan","Gauhar"]
    math_grade=[84,98,78,91]
    history_grade=[96,80,76,90]
    programming_grade=[78,64,86,89]
    for i in range(len(students)):
        if name==students[i]:
            print(students[i]+"'s grades:")
            print("Math grade:"+str(math_grade[i]))
            print("History grade:"+str(history_grade[i]))
            print("Programming grade:"+str(programming_grade[i]))

printAll("Akzhan")


