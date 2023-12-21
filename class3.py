student = "joshua"
studentlist = ["joshua","habeeb","mr money","da tomiwa"]
"""Array is a collection of item and it is divided into 4 groups
(list, tuple,set,dictionary)
list= ordered, mutable
tuple = ordered, immutable
set = unordered, mutable
dictionary = ordered, mutable, comes in pair i.e (key:value)"""
print(studentlist[-2][3:])
studentlist[-2] = "samuel"
print(studentlist)
print(len(studentlist))
#method-append, insert,remove, method,pup
# variable.metho()
"""append()	Adds an element at the end of the list
ce elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""
studentlist.pop(2)
print(studentlist)
studentlist.append("parach")
print(studentlist)
fruit = ("apple","banana","oranges")
print(fruit)
print(fruit[2])
studentlist.insert(0,fruit[0])
print(studentlist)
studentlist.append(fruit[-1])
print(studentlist)
studentlist.insert(len(studentlist)//2,fruit[1])
print(studentlist)
studentlist.extend(fruit)
print(studentlist)







