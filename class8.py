#function is a block of codes thhat is reusable
#only runs when invoked
#can accept data 
#can return data as output
#def is used to create a function
#parameter - requirement

"""def greetings():
    print("Hello World")
greetings()"""

def greeting():
    name = "parach"
    print("hello" , name)
name = "mr money"
def greeting2(person):
    school = "university of ibadan"
    print(f"{person} attended {school}")
    print(f"{name} is a friend to {person}")

def add_nums(num1,num2):
    print(num1 + num2)
def sub_nums(num1,num2):
    print(num1 - num2)
def divide_nums(num1,num2):
    print(num1 / num2)
def multiply_nums(num1,num2):
    print(num1 * num2)
dollar_rate = 1100
def dollartonaira(dollaramount):
    print(dollar_rate * dollaramount)
def nairatodollar(nairaamount):
    print(round(nairaamount / dollar_rate,2))




greeting()
greeting2("Tade")
add_nums(1,2)
add_nums(4,25)
sub_nums(234,456)
divide_nums(23,34)
multiply_nums(3,45)
dollartonaira(100)
nairatodollar(500000)

