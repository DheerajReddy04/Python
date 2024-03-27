'''
class student():
    names = []
    def namess(self,name):
        student.names.append(name)
stu1 = student()
stu1.namess('xyz')
stu2 = student()
stu2.namess('Dheeraj')
print(student.names)
'''

'''
class score():
    def marks(self,math,english,chemistry):
        dict = {'math':math,'english':english,'chemistry':chemistry}
        print(dict)
        if math < 50 or english<50 or chemistry < 50:
            print("fail")
        else:
            print("pass")
    def total(self,math,english,chemistry):
        print("Total: {}".format(math+english+chemistry))
mark_ref = score()
mark_ref.marks(60,69,69)
total_ref = score()
total_ref.total(60,69,69)
'''

'''
class Student():
    def __init__(self,name1,name2,name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    
    def names(self):
        dict = {'name1': self.name1,'name2': self.name2,'name3': self.name3}
        print(dict)
printnames = Student('Ganesha','Jesus','Allah')
printnames.names()
printnames2 = Student('Dheeraj','Azmath','Giri')
printnames2.names()
'''
'''
Name
ind scorre obj Attribute
total score class attribute
no of 50s and 100s


shopkeeper
buy individual products and find total amount for each product
'''

'''
class score():
    total = 0
    def __init__(self,ind_score):
        self.ind_score = ind_score
        score.total += self.ind_score
for i in range(1,12):
    player_score = int(input(f"Enter {i} player's score"))
    instance = score(player_score)
print(score.total)
'''

'''
class Cricket():
    total = 0
    def __init__(self,ind_score,achievements):
        self.ind_score = ind_score
        Cricket.total += self.ind_score
score_instance = []
for i in range(1,12):
    player_score = int(input(f"Enter {i} player's score"))
    instance = Cricket(player_score)
    score_instance.append(instance)
print(Cricket.total)
ask_achievements = Cricket()
'''

'''
class Student:
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch
    def _display(self):
        print(self.name,self.roll,self.branch)
obj = Student("Dheeraj",6,"Cse")
obj._display()
'''

'''
class Student():
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch
    def _display(self):
        print(self.name,self.roll,self.branch)
obj = Student("Dheeraj",6,"Cse")
#obj._display()

class Marks(Student):
    def __init__(self):
        pass
    def marksubject(self,math,english,chemistry):
        self.math = math
        self.english = english
        self.chemsitry = chemistry
    def totalavg(self):
        total = self.math+self.english+self.chemsitry
        avg = total/3
        print(total,avg)
        c1=Student._display(self)
        print(c1)
obj1 = Marks()
obj1.marksubject(10,20,30)
obj1.totalavg()
'''