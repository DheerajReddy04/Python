'''
#question 1 EBOX
class Person():
    def __init__(self):
        name = input("Enter Name:")
        age = input("Enter Age:")
        self.name = name
        self.age = age
        print("Person Details",self.name,self.age,sep='\n')
obj = Person()
'''

'''
#question 2 EBOX
class Person():
    __name = None
    __age = None
    def __init__(self):
        name = input("Enter Name:")
        age = input("Enter Age:")
        self.__name = name
        self.__age = age
    def display(self):
        print("Personal Details",self.__name,self.__age,sep='\n')
obj = Person()
obj.display()
'''

'''
#question 3 EBOX
#The __str__() method is invoked when we print the obj of the class or use the str() function
class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__name} is {self.__age} years old."
name = input("Enter Name: ")
age = int(input("Enter Age: "))
obj = Person(name,age)
print(obj)
'''

'''
#question 4 EBOX
class Person():
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.full_name = self.fullname()
    
    def __str__(self):
        return f"Full name of the person is {self.full_name}\nPerson Details\n{self.full_name} is {self.__age} years old and her email id is {self.__first_name}.{self.__last_name}@gmail.com"
    
    def fullname(self):
        return self.__first_name + ' ' + self.__last_name
first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")
age = int(input("Enter age: "))
obj = Person(first_name,last_name,age)
print(obj)
'''

'''

#wrong code
i=0
class Person():
    count = 0
    domain_name = input("Enter domain name: ")
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.full_name = self.fullname()
        Person.count  += 1
    
    def __str__(self):
        if Person.count == 1:
            self.number = 'First'
        elif Person.count == 2:
            self.number = 'Second'
        return f"{self.number} Person Details\nFull name of the person is {self.full_name}\n{self.full_name} is {self.__age} years old and her email id is {self.__first_name}.{self.__last_name}@{self.domain_name}"
    
    def fullname(self):
        return self.__first_name + ' ' + self.__last_name
first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")
age = int(input("Enter age: "))
obj1 = Person(first_name,last_name,age)
obj2 = Person(first_name,last_name,age)
print(obj1)
print(obj2)
'''


'''
#question 5 EBOX
class Person():
    count = 0  # Class variable to keep track of instances

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.full_name = self.fullname()
        Person.count += 1  # Increment count on each initialization
        self.instance_number = Person.count  # Instance specific count

    def __str__(self):
        if self.instance_number == 1:
            self.number = 'First'
        elif self.instance_number == 2:
            self.number = 'Second'
        # You can extend this logic for more instances

        return f"{self.number} Person Details\nFull name of the person is {self.full_name}\n{self.full_name} is {self.__age} years old and his/her email id is {self.__first_name}.{self.__last_name}@{Person.domain_name}"

    def fullname(self):
        return self.__first_name + ' ' + self.__last_name

domain_name = input("Enter domain name: ")

# First Person's details
print("Enter details of first person")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))
obj1 = Person(first_name, last_name, age)

# Second Person's details
print("Enter details of second person")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))
obj2 = Person(first_name, last_name, age)

Person.domain_name = domain_name  # Setting domain_name as a class attribute

print(obj1)
print(obj2)
'''