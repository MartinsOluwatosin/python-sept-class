"""x = 50
y = 20

if x > y :
    print("x is greater than y")
else : 
    print("y is greater than x")

comparison operators : 
  >,<, ==, !=, .=>, <=

logical operators: and, not, or

if (x!=y) or (x<y):
    print("x is greater")
else : 
    print("y is great")

if (x == y) and (x < y) :
    print("x is greater")
else:
    print("y is greater")

if x == y :
    print("x is equal to y")
elif x > y :
    print("x is greater")
elif x < y :
    ("x is lesser")
else :
    print("value of x is invalid")"""


""" C - Create
    R - Read
    U - Update
    D - Delete"""

score = input("input your score : ")

"""if score.isnumeric():
    score = int(score)
    if score < 0 or score > 100 :
        print("\n\n==========")
        print("You have entered invalid score.\nEnter a value between 0 - 100")
        print("==========\n\n")
    else:
        if score < 40 :
            print(f"student grade for {score} - F9")
        elif score < 45 :
            print(f"student grade for {score} - E8") 
        elif score < 50 :
            print(f"student grade for {score} - D7")      
        elif score < 55 :
            print(f"student grade for {score} - C6")
        elif score < 60 :
            print(f"student grade for {score} - C5")
        elif score < 65 :
            print(f"student grade for {score} - C4")
        elif score < 70 :
            print(f"student grade for {score} - B3")
        elif score < 75:
            print(f"student grade for {score} - B2")
        else:
            print(f"student grade for {score} A1")                         
else : ("input contains other characters")"""

#using loop now
grade = [40,45,50,55,60,65,70,75]
result = ["f9","E8","D7","C6","C5","C4","B3","B2","A1"]



if score.isnumeric():
    score = int(score)
    if score < 0 or score > 100 :
        print("\n\n==========")
        print("You have entered invalid score.\nEnter a value between 0 - 100")
        print("==========\n\n")
    else:
        for mark in grade : 
            index = grade.index(mark)
            if score < mark :
                print(f"student grade for {score} - {result[index]}")
            else: print(f"student grade for {score} - {result[-1]}")
            break
else :
    print("input contains invald characters")



      

    

