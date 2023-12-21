#expression is piece of code that produces value

"""name = "John Smith"
age = 20
admission_status = "new"
is_new = True 
ask two questions ; a persons name and favourite colour. then, print a message like mosh likes blue
name = input("What is your name: ")
fav_color = input("What is your favorite color: ")
print(f"{name} likes {fav_color}")
print(name + " likes " + fav_color)

write a code to claculate age
birth_year = int(input("When where you born? "))
age = 2023 - birth_year
print(age)

ask a user their weight in pounds convert to kilogram and print
weight = input("whats your weight in pounds? ")
convert = 0.45 * float(weight)
print(f" you are  {convert}  kg ")"""
#AUGMENTED ASSIGNMENT OPERATOR: +=
x = 2.9
#print(round(x))
#print(abs(-2.9))
"""name = "moshwan"
length = len(name)
if length < 3:
    print("name must be at least 3 character long")
elif length > 50:
    print("name can be a maximum of 50 characters")
else: 
    print("name looks good")"""

"""weight = (input("what is your weight: "))
weight_type = input("(L)bs or (K)g: ").upper()
if weight.isdigit():
    if weight_type == 'K':
        convert = 0.45 * int(weight)
        print(f"YOU ARE {convert} KILOS")
    elif weight_type == 'L':
        convert = int(weight) / 0.45
        print(f"YOU ARE {convert} POUNDS")
    else: print()
else : print('ENTER VALID WEIGHT')"""

"""i=1
while i <= 5:
    print('*' * i)
    i += 1
print('done')"""

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You got it right")
        break
else: print("sorry you failed!")
