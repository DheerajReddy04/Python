'''
def slant():
    for i in range(5):
        for u in range(i+1):
            print(u, end=" ")
        print("\n")
slant()
'''
#to print a square
'''
def square(a):
    for i in range(a):
        for u in range(a):
            if( i == 0 or i == a-1 or u == 0 or u == a-1):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()
a = int(input("Enter the square side"))                    
square(a)
'''
def square(a):
    for i in range(a):
        for u in range(a):
            if( i == 0 or i == a-1 or u == 0 or u == a-1):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()
def name(a):
    for i in range(a):
        for u in range(a):
            if(i == u and i):
                if(i == u == True):
                    print("*", end=" ")
a = int(input("Enter the square side"))                 
square(a)
name(a)