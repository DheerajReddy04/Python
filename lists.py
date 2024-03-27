#Lists
thislist = ["apple","cherry","banana","orange","watermelon","sapota"]
#A list can contain different data types:
thatlist = ["apple",30,"banana",True]
charlist = ["hi","hello","bye","fame","tear"]
numlist = [1,3,5,7,8,6,4,2]
#lists are defined as objects with the data type 'list'
print(type(thislist))
#list can also be made using list constructor list()
herelist = list(("apple","banana"))
#Slicing is also possible to add a new objects: here apple will be replaced with orange and watermelon
herelist[1:2] = ["orange","watermelon"]
print(herelist)
#append() to add an object at the end of the list
thatlist.append("xyz")
print(thatlist)
#insert() syntax: list.insert(number,object); inserts at the specified place
thatlist.insert(1,"sample text")
print(thatlist)
#to append a list,tuple,set or dictonary to another list, we use extend()
thislist.extend(thatlist)
print(thislist)

#removing objects from the list
#remove() methood ; removes the specified object of hte list
thislist.remove("apple")
print(thislist)
#pop() method ; removes the specified index, if no index is provided, then the last object will be removed
thislist.pop(2)
print(thislist)
#del keyword ; removes the specified item or the whole list itself
del thislist[0]
print(thislist) 
#del thislist #removes the whole list
#clear() method ; removes all the items/objects in the list but the list itself will not be deleed. It will be an empty list
thatlist.clear()
print(thatlist)

#looping a list
#for loop(there is no need for updation operator in forloop but we do need a updation operation in while loop)
print("For loop")
for i in thislist:
    print(i)
for i in range(len(thislist)):
    print(thislist[i])
#while loop (we do not have to initialize the forloop variable but we do have to initialize the whileloop variable)
print("While loop")
x =0
while(x < len(thislist)):
    print(thislist[x])
    x = x+1

#List Comprehension; It allows us to write long operations on list in a single line
#syntax; [newlistvariable = expression for item in iterable if condition == True]
#here expression is the current item in iteration and also the outcome. we can manipulate it before it reaches newlist.
#item is the variable item which we are using
#iterable can be anything like a list, tuple, set etc and we can also use range() function in it
#condition is optional 
print("List Comprehension") #make sure that no integer objects are in the list if you are manipulating the expression before placing in newlist. not needed to check otherwise
newlist = [x for x in range(10) if x != 3]
print(newlist)
newlist = [xvar.upper() for xvar in charlist if xvar !="banana"]
print(newlist)
#we can also include condition in the expression but it wouldn't be as a consitional statement but as a way to manipulate the outcome
#here the code says 'return the item if its not hi, if it is hi then return namaste'
newlist = [xvar if xvar != "hi" else "namaste" for xvar in charlist]
print(newlist)

#Sorting lists
#sort() method is used to sort list alphanumerically
print("Sorting Lists")
#we can't put sort method inside print as it first needs to sort the list and then it can be printed. Don't do this print(newlist.sort()) 
charlist.sort()
print(charlist)
numlist.sort()
print(numlist)
# we can sort the list in descending order using reverse = True keyword argument 
charlist.sort(reverse = True)
print(charlist)
numlist.sort(reverse = True)
print(numlist)
#we can customize our own function using key = function keyword argument
#here we are using func and key = function keyword argument to sort the numbers interms of closest to 4 
def func(n):
    return abs(n - 4)
numlist.sort(key = func)
print(numlist)
#sort() method is case sensitive. it can give unexpected outcomes sometimes. so we have to convert the lsit to lowercase using key = str.lower
#str.lower is akeyword function which converts string to lowercase
newlist = [xvar.upper() for xvar in charlist]
print(newlist)
newlist.sort(key = str.lower)
print(newlist)
#The reverse() method reverses the current sorting order of the elements.
newlist.reverse()
print(newlist)

#Copy Lists-We cant directly copy by using list2 = list1 as list2 will only be areference to list1 and any changes made to list1 will also be made to list2
print("Copying Lists")
#two way to copy a list
#first is built in List method copy() {preffarable as easy to remember}
copylist = charlist.copy()
print(copylist)
#another method is t ouse bulilt in method list()
copylist2 = list(thislist)
print(copylist2)

#Join Lists
print("Joining Lists")
#directly adding
joinlist = thislist + newlist
print(joinlist)
#using append() method- this method adds one item at time and needs a for loop to add all the items in the list. It is better when we have to add only one item
for xvar in thislist:
    newlist.append(xvar)
print(newlist)
#using extend() method-this method adds all the items/parameters supplied to it at once and does not need for variable. It is better when we have to add many items
thislist.extend(newlist)
print(thislist)
newlist.extend(range(10))
print(newlist)
newlist.insert(10,"abfvbsehvbaelvba")
print(newlist)
newlist.pop(10)
print(newlist) 

#List methods(some of them have been already implemented above)
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of times an item repeated with the specified value
x = newlist.count("banana")
print(x)
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
x = newlist.index("banana")
print(x)
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list