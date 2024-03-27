#prime or not with fucntions
'''
def prime():
    a = int(input("Enter a number:"))
    count = 0
    for i in range(1,a+1):
        if a%i == 0:
            count += 1
    if(count == 2):
        print("It is prime")
    else:
        print("Not prime")
prime()
'''

#reverse a number using function
'''
def rev():
    a = int(input("Enter a number:"))
    temp = a
    reverse = 0
    while temp > 0:
        temp %= 10
        reverse = reverse * 10 + temp
        a //= 10 # / gives float and // gives int
        temp = a
    print(reverse)
rev()
'''

#factorial with recursion
'''
def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
a = int(input("Enter a number:"))
b = factorial(a)
print(b)
'''
#fibonacci with recursion
'''
def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
a = int(input("Enter a number"))
for i in range(a):
    print(fibonacci(i),end=" ")
'''