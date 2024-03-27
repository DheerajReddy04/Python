# https://w3resource.com/python-exercises/python-basic-exercises.php
#program to find python version
 #import sys
 #print(sys.version)
#program to print date and time
 #import datetime
 #now = datetime.datetime.now()
 #print("The current date and time are")
 #print(now.strftime("%Y-%m-%d %H:%M:%S"))
#program to calculate area of a circle by taking radius
 #radius = int(input("Enter radius: "))
 #print("The area of the circle is", 3.14 * radius *radius)
#take first and last name and print in reverse ordersd
 #firstname = input("Enter your first name: ")
 #lastname = input("Enter your last name: ")
 #print(lastname+" "+firstname)

#list = [50,10,100,120,100,100,120,5,10,11,12]
#for i in list:
#    if(i >= 100):
#        print(i)


#list = []
#n = int(input("Enter number of elements : "))
#for i in range(0, n):
#    var = int(input())
#    list.append(var) 
#print("The numbers above 100 in the given list are:")
#for i in list:
#    if(i >= 100):
#        print(i)

#fibonacci series
'''
def fib():
    first, second = 0,1
    x = int(input("Enter the starting range:"))
    y = int(input("Enter the ending range:"))
    if x == 1 and y ==1:
        print(first)
    elif x == 1 and y == 2:
        print(first,second)
    else:
        print(first, second)
        for i in range(x,y):
            nextterm = first+second
            print(nextterm)
            first = second
            second = nextterm
fib()
'''
#code to print the number having equal number of 2's, 4's and 8's in a given range
'''
def num248():
    a = int(input("Enter starting range:"))
    b = int(input("Enter ending range:"))
    for i in range(a,b):
        numstr = str(i)
        count2, count4, count8 = 0,0,0
        for x in numstr:
            if x == '2':
                count2 += 1
            elif x == '4':
                count4 += 1
            elif x == '8':
                count8 += 1
            if count2 == count4 == count8 == True:
                print(i)
num248()
'''
#variable length argument
'''
def add(x,*num):
    z = x + num[0]+num[1]
    print(z)
add(5,2,4)
'''

#keyword and variable length argument
'''
def add(**num):
    z = num['a']+num['b']+num['c']
    print(z)
add(a=1,b=2,c=3)
'''
'''
#program to print the largest prime palindrome in a given range
start = int(input("Enter starting from:"))
end = int(input("Enter ending at:"))
while start < end:
    i = 2
    count = 0
    if(start%i==0):
        count += 1
        i += 1
    if(count == 1):
        print(start)
    start += 1
    '''


'''
def prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i += 2
    return True
def palindrome(number):
    original_number = number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10
    return original_number == reverse_number
def find_largest_prime_palindrome(start, end):
    prime_palindrome = None
    number = end
    while number >= start:
        if prime(number) and palindrome(number):
            prime_palindrome = number
            break
        number -= 1
    return prime_palindrome
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = find_largest_prime_palindrome(start, end)
if result is not None:
    print(f"The largest prime palindrome number in the range [{start}, {end}] is: {result}")
else:
    print(f"No prime palindrome number found in the range [{start}, {end}].")
'''

def prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i += 2
    return True
def palindrome(number):
    return number == number[::-1]
def find_largest_prime_palindrome(start, end):
    prime_palindrome = None
    number = end
    while number >= start:
        if prime(number) and palindrome(str(number)):
            prime_palindrome = number
            break
        number -= 1
    return prime_palindrome
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = find_largest_prime_palindrome(start, end)
if result is not None:
    print(f"The largest prime palindrome number in the range [{start}, {end}] is: {result}")
else:
    print(f"No prime palindrome number found in the range [{start}, {end}].")
