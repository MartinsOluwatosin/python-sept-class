#set array
setlist = {"Banana","Apple"}
setlist.add("Papaya")
print(setlist)
setlist2 = {"Banana","Mango","orange"}
setlist.difference(setlist2)
print(setlist)
setlist2.difference(setlist)
print(setlist)
x={"we", "saw","came"}
y={"we", "not", "come"}
x.difference(y)
print(x)
y.difference(x)
print(y)
x1 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z = x1.difference(y2)
print(z)
y2.difference(x1)
print(y2)





#PYTHON DICTIONARY {key:value}
#unordered,mutable and indexed
student1 = {
    "name" : "samuel",
    "age" : 52,
    "favorite" : "programming",
    "status" : "divorced",
    "genotype" :"AA",
    "location": "ibadan",
    "sibliings" : ["joshua","mr money","mr tolu"]}

print(student1)
print(type(student1))
print(student1["location"])

student2 = {
    "name" : "John",
    "age" : 16,
    "favorite" : "football",
    "status" : "single",
    "genotype" :"As",
    "location": "kano",
    "sibliings" : ["jude","ronaldo","messi"]}

print(student2)

student3 = {
    "name" : "mudryk",
    "age" : 21,
    "favorite" : "tennis",
    "status" : "married",
    "genotype" :"AA",
    "location": "Ukraine",
    "sibliings" : ["Sterling","Neymar","Enzo"]}

print(student3)

studentlist = [student1,student2,student3]
print(studentlist)
print(type(studentlist))
print(studentlist[1]["name"])

print(studentlist[0]["sibliings"][1][3:].upper())


#LOOP IN PYTHON

for x in studentlist :
     print(x["name"])
     print(x["sibliings"])
     sibliings = x["sibliings"]
     print(sibliings)
