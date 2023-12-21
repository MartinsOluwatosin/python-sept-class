fruitlist = ["banana", "apple", "mangoes", "orange", "pawpaw"]
for fruit in fruitlist:
    #print(fruit.upper())

school = "parach"
for x in school:
    #print(x,school.index(x))

list = "samuel"
for eachletter in list:
    #print("i am a boy " + eachletter)

for x in range (0,10):
    #print("Hello King")


student1 = {
    "name" : "samuel",
    "age" : 52,
    "favorite" : "programming",
    "status" : "divorced",
    "genotype" :"AA",
    "location": "ibadan",
    "sibliings" : ["joshua","mr money","mr tolu"]}

"""print(student1)
print(type(student1))
print(student1["location"])"""

student2 = {
    "name" : "John",
    "age" : 16,
    "favorite" : "football",
    "status" : "single",
    "genotype" :"As",
    "location": "kano",
    "sibliings" : ["jude","ronaldo","messi"]}

#print(student2)

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

for x in studentlist:
    print("Hello " +x["name"]+" welcome to " + school.upper())

