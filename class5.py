#creating a topple list and adding them together without the use of extend
tuple1 = ("parach","joshua", 42, ["hello, world"])
tuple2 = (1,2,3,4,5)
tuple3 = tuple1 + tuple2
print(tuple3)

for x in tuple1:
    print(x)

str1 = ""
for x in tuple1:
    str1+= str(x) + ","

print(str1)
print(str1.split(","))

mathresult = input("Enter student math result : ")
englishresult = input("Enter student math result : ")
result = int(mathresult) + int(englishresult)
print(result)

x = 5
while x < 10 :
    print(x)
    
