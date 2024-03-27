import sys
print(sys.version)
#basic print for strings
print("hi")
print("hello")

#assigning a string to a variable by using single quotes and double quotes
q = "hello, google"
r = 'hello, youtube'

#a = str(10)
#assignig a int value to a variable
a = 30 
b = 20
c = 10

#typecasting int a to float a
#if a has different values, then the latest value of a will be considered in the operations
#a = float(10)
#we can directly convert a into float without any confusion by doing this
a = float(a)

#printing the variable
print(q)

#printing the nth byte of the variable(a string is a array)
print(q[4])

#printing the length of the variable using len 
print(len(q))

#finding the datatype of the variable using type
print(type(q))
print(type(a))

#d = input("Enter d")
#print(d)

#calculating sum of two int
print("Sum of a and b is", a+b)

#using if elif and else conditions
if a > b :
    print("a is bigger")
elif b > a :
     print("b is bigger")
else :
    print("Both are equal")

#string is a array and it can be operated like an array. Here it starts from 2nd byte and prints till the n-1 byte which is 5
#This is called slicing of the string
print(q[2:6])
#starting to the n-1 byte will be printed
print(q[:6])
#from the nth byte to the last byte will be printed
print(q[2:])
#basically prints the whole string from 0th byte to the n-1 byte which is the last byte
print(q[:])

#modifying strings using uppercase, lowercase and split[it takes a parameter and splits the string and writes it in the form of a list], strip[The strip() method removes any whitespace from the beginning or the end:])
print(q.upper())
print(q.lower())
print(q.split("o"))
print(q.strip())

#concatenate strings
print( q +" "+ r)

#We noramally can not add a string and a integer together
#ex : t = "my name is dheeraj and my age is " + age  [doesnt work]
#here we use format method to insert anytype of datatype into a string and it formats it to fit it in.
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
item = 2
price = 100
order = "I want to buy {0} items each of {1} ruppees"
print(order.format(item,price))

#If we want to use double quotes inside double quotes, we have to use escape character \ between the word to not encounter errors
#the code will not work if you directly want to print instead of supplying it as a varibale
#ex :  print("My name is Dheeraj and not \"Diraj\".")  will not work and show an indentation error
example = "My name is Dheeraj and not \"Diraj\"."
print(example)

#String methods is in seperate file

#About boolean values
#normally print(condition) returns a boolean value
print(10>9)
#The bool() function allows you to evaluate any value, and give you True or False in return
#bool function returns True if that variable has any content in it. If we provide None, (), {}, [], then we get False value
print(bool(a))
print(bool(()))

#Python Operators
#arithmetic operators +  -  *  /  %(modulus)  **(exponential)  //(floor division)
print("Arithmetic Operators")
print("Addition of a and b is ",a+b)
print("SUbtraction of a and b is ",a-b)
print("Multiplication of a and b is ",a*b)
print("division of a and b is ",a/b)
print("modulus of a and b is ",a%b)
print("floor division of a and b is ",a//b)
#assignment operators = , +=, -=, *=, /=, %=, **=, //=, &=(bitwise and =), |=(bitwise or =), ^=(bitwise xor =), >>=(bitwise right shift), <<=(bitwise left shift)
    #and- both the values are 1, then it will be 1
    #or- atleast one value is 1, then it will be 1
    #xor- only one 1, then 1 else if both 1 and both 0, then 0
#assignment operators ==, !=, >, <, >=, <=
#logical operaators and(instead of && in c) , or(instead of || in c), not(reverses the output)
print("Logical operators")
print(a >50 and b > 50)
print(a >15 or b>15)
print(not(a>50 or b>5))
#identity operator is, is not - checks if both the objects are same i.e have same memory locationa and not if they are equal
print("Identity Operators")
print(a is a)
print(a is b)
#membership operators in , not in
    #in- returns true if the first object is present in the second objet
    #not in- returns true if the first object is not present in the second object
print("Membership Operators")
print("hello" in q)
print("hi" in q)
#bitwise operators &(and), |(or), ^(nor), ~(not), >>(right shift), <<(left shift)
    #not-inverts all the bits considering 16 bits ex: 0000000000000001 turns to 1111111111111110