#University of ibadan requires student to hav 50 and above in english and math to gain admission
myname = input("Wetin be ya name: ")
namex = myname + " Welcome to the University Of Ibadan"
print(namex.title())
englishresult = input("Wetin you score for english: ")
mathresult = input("Wetin you score for math: ")
x = englishresult
y = mathresult


if x.isnumeric() and y.isnumeric():
    score1 = int(x)
    score2 = int(y)
    summ = score1 + score2
    if score1 > 100 or score2 > 100:
        print("\n\n==========")
        print("YOU DEY ALRIGHT?.\nEnter values between 0 - 100")
        print("==========\n\n")
    elif score1 >= 50 and score2 >= 50 :
        print(f"YOUR TOTAL SCORE NA {summ}. CONGRATULATIONS WE GO ADMIT YOU!!!!")
    else : print(f"YOUR TOTAL SCORE NA {summ}. TRY AGAIN NEXT YEAR, YOU BE OLODO!!!")

        
else : print("NA ONLY NUMBER YOU FIT TYPE FOR HERE")
     
  
    
