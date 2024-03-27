#A set is a collection which is unordered, unchangeable, and unindexed. But we can remove and add items. Sets do not allow duplicate values
#They are represented in curly braces
thisset = {"apple","banana","orange"}
print(thisset)
#Set takes True, 1 and False, 0 as the same value. So any one value is printed and mostly the one which was first written in the stack
tfset = {True,1,0,False}
print(tfset)

#length of a string
print(len(thisset))

#type of a set is a 'set'
print(type(thisset))

#we can use the set consstructor set() to build a set
newset = set(("new","set"))
print(newset)

#we cannot access items by refering to the indexing or key, but we can loop through the set
for x in newset:
    print(x)
# we can check if an item is in the set using 'in' keyword
print("banana" in thisset)

#add() method is used to add an item to the set. As set is unordered, we will not know where the item is added
newset.add("add")
print(newset)
#to add one set to the current set, we use the update() method. The object inside the update() method can be iterable pbjects like list, tuples, dictionaries
thisset.update(newset)
print(thisset)
thislist = ["1234",1]
thistuple = ("4321",4)
newset.update(thislist)
print(newset)
newset.update(thistuple)
print(newset)

#removing items from the set
#remove() method and discard() are used to remove an item from the list. 
#the only difference is that the remove method gives an error when the item to be removed doesnot exist in the set but the discard method deoesn't
#newset.remove("ab")  
#This is the error
#    newset.remove("ab")
#KeyError: 'ab'
newset.remove("4321")
print(newset)
newset.discard("ab")
newset.discard("1234")
print(newset)
#pop() method can be used to remove a random item as we cannot provide the index. The return value of the pop() method is the removed item
x = newset.pop()
print(x,newset)
#clear() method clears the entire set
#newset.clear()
#print(newset)
#del keyword deletes the whole set. it will show error to print the set
#del newset
#print(newset)