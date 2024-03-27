#A tuple is a collection which is ordered and unchangable
# to make a tuple with only one tuple, we have to use a comma after the the item. Else it won't be considered a tuple
mytuple = ("banana",)
#type() of a tuple is 'tuple'
print(type(mytuple))
#tuple construtor - tuple() method to make a tuple
tuplecon = tuple(("hi","bye","hello"))
thistuple = ("banana","apple","orange","guava")
print(tuplecon)

#accesing tuples, negative indexing, range of indexes, range of negative indexing is same as Lists
#check if item exists in list
if "hi" in tuplecon:
    print("YES")

#to change a tuple, we have to convert the tuple to list, modify the values, and then convert back to tuple
x = list(thistuple)
x[2] = "apple"
thistuple = tuple(x)
print(thistuple)

#add items
#1. Add by converting to list then back to tuple
#2. Add two tuples; adding tuples is allowed 
thistuple += mytuple
print(thistuple)

#remove items
#1. Convert to list, remove item by using remove() method, then convert the list back to tuple
x = list(thistuple)
x.remove('apple')
thistuple = tuple(x)
print(thistuple)
#2.delete the complete tuple using del keyword
#del thistuple

#unpacking tuple
#packing- assigning values when creating a tuple
#unpacking- extract the values back into variables
(q,w,e,r) = thistuple
print(q)
print(w)
print(e)
print(r)
# we can add * symbol if the number of variables is less than the number of values
print("When the number of variables are less than the number of values")
(a,s,*d) = thistuple
print(a)
print(s)
print(d)

#looping through a tuple is similar to that of list
#for loop
#for x in thistuple
#for i in range(len(thistuple))
#while loop
#while i <= len(thistuple)

#Joining tuples
#1. add two tuples
atuple = (1,2,3,3)
btuple = ("a","b","c","d")
abtuple = atuple + btuple
print(abtuple)
#2. Multiply tuples
#multiply the contents of the same tuple into an other tuple
anothertuple = abtuple * 2
print(anothertuple)

#tuple only has two methods in python
#1. count()
print("count of banana in thistuple")
count = thistuple.count("banana")
print(count)
#2. index()
print("index of apple in thistuple")
index = thistuple.index("apple")
print(index)