"""state_capital = {
    "Ondo" : "Akure",
    "Lagos" : "Ikeja",
    "Oyo" : "Ibadan",
    "Ekiti" : "Ado-ekiti",
    "Osun" : "Osogbo"
}

inputt = input("Choose any option from A-D: ")
if inputt == "A" or "a":
    state = input("Enter the name of a state: ")
    capital = input("Enter the capital of the state: ")
    
    print("info succesfully added")
    print(state_capital)
else:
    if inputt == "B" or "b":
        for state, capital in state_capital:
            print(f"{state}: {capital}")"""



Nigeria = [
    {"state" : "Ondo",
    "capital" : "Akure"},
    {"state" : "Ebonyi",
    "capital" : "Abakaliki"},
    {"state" : "Taraba",
    "capital" : "Jalingo"},
    {"state" : "Delta",
    "capital" : "Asaba"},
    {"state" : "Akwa-ibom",
    "capital" : "Uyo"}

]
print("Enter option A - D")
print("A to view the list")
print("B to create a state and capital")
print("C to edit a state and capital")
print("D to delete a state and capital \n")
user_input = str(input("Enter your option: ")).casefold()

if user_input == "a" :
    numbering = 0
    for item in Nigeria:
        numbering+=1
        print(f"{numbering}- The state - {item['state']},the capital - {item['capital']}")

elif user_input == "b" :
    state = (input("Enter the new state: "))
    capital = (input(f"Enter the capital of {'state'}: "))
    new_state_capital = {
        "state" : state,
        "capital" : capital,
    }
    Nigeria.append(new_state_capital)
    numbering = 0
    for item in Nigeria:
        numbering+=1
        print(f"{numbering} - The state - {item['state']},the capital - {item['capital']}")

elif user_input == "c":
    numbering = 0
    for item in Nigeria:
        numbering+=1
        print(f"{numbering} - The state - {item['state']},the capital - {item['capital']}")
    edit_number = input("Enter the number of state to edit: ")
    if edit_number.isnumeric():
        targetstate = Nigeria[int(edit_number)-1]
        print(targetstate)
        state = input("Enter the right state: ")
        capital = input("Enter the right capital: ")
    
        if state:
            targetstate["state"] = state
        if capital:
            targetstate["capital"] = capital
        numbering = 0
        for item in Nigeria:
            numbering+=1
            print(f"{numbering} - The state - {item['state']},the capital - {item['capital']}")
    else: print("can only enter numbers")
        
    
elif user_input == "d":
    numbering = 0
    for item in Nigeria:
        numbering+=1
        print(f"{numbering} - The state - {item['state']},the capital - {item['capital']}")
    delete_number = input("Enter the number of state to delete: ")
    if delete_number.isnumeric():
        Nigeria.pop(int(delete_number)-1)
        numbering = 0
        for item in Nigeria:
            numbering+=1
            print(f"{numbering} - The state - {item['state']},the capital - {item['capital']}")
    else: print("can only enter numbers")