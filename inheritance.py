#Display the salary and perosnal details of 5 employees using Single Inheritance
'''
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

class PrintDetails(Employee):
    count = 0
    def __init__(self,name,age,salary,gender):
        super().__init__(name,age,salary)
        self.gender = gender
        PrintDetails.count += 1
    def display(self):
        if PrintDetails.count == 1:
            detcount = "First"
        elif PrintDetails.count == 2:
            detcount = "Second"
        elif PrintDetails.count == 3:
            detcount = "Third"
        elif PrintDetails.count == 4:
            detcount = "Fourth"
        else:
            decount = "Fifth"
        
        print(f"{detcount} person details")
        print("Name:",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Gender: ",self.gender)
for i in range(5):
    print("Enter details")
    name = input("Enter name")
    age = input("Enter age")
    salary = input("Enter salary")
    gender = input("Enter gender")
    print_det = PrintDetails(name,age,salary,gender)
    print_det.display()
'''

# WAP that extends the class Result so that the final result of the student is evaluated based on the marks obtained in the test.
'''
class Result:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

class Extend(Result):
    def final_display(self):
        if int(self.marks) > 50:
            print("Pass")
        else:
            print("Fail")
name = input("Enter name: ")
age = input("Enter age: ")
marks = int(input("Enter marks: "))
res = Extend(name,age,marks)
res.display()
res.final_display()
'''

class A:
    def add(a,b):
        print(a+b)
class B(A):
    def sub(a,b):
        print(a-b)
obj = B
obj.add(10,5)

