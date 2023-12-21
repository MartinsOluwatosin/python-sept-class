naija_states = [
    {"state": "Edo",
    "capital" : "Benin"},
    {"state": "Lagos",
    "capital" : "Ikeja"},
    {"state": "Ebonyi",
    "capital" : "Abakaliki"},
    {"state": "Ekiti",
    "capital" : "Ado-Ekiti"},
    {"state": "Imo",
    "capital" : "Owerri"},
    {"state": "Jigawa",
    "capital" : "Dutse"},
    {"state": "Kogi",
    "capital" : "Lokoja"}
]

print("Select any option from A - D")
print("A - you go fit view wetin dey the list")
print("B - you go fit create a new addition to the list")
print("C - you go fit edit something wey dey the list")
print("D - you go fit comot something from the list")
inputt = (input("Which one you wan choose: ")).upper()

if inputt == "A" :
    position = 0
    for details in naija_states:
        position += 1
        print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")
   
elif inputt == "B" :
    state = input("Enter a new state: ").capitalize()
    capital = input("Enter a new capital: ").capitalize()
    newdetails = {
        "state" : state,
        "capital" : capital
    }
    if newdetails in naija_states:
        print("Already Exists!!")
    else:
        naija_states.append(newdetails)
        position = 0
        for details in naija_states:
            position += 1
            print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")

elif inputt == "C" : 
    position = 0
    for details in naija_states:
        position += 1
        print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")
    state_edit = (input("Enter the position of wetin you wan edit: "))
    if state_edit.isnumeric() :
        action = naija_states[int(state_edit) -1]
        print(action)
        rightstate = input("Wetin be the correct state name: ").capitalize()
        rightcapital = input("wetin be the correct capital name: ").capitalize()
        if rightstate:
            action["state"] = rightstate
        if rightcapital:
            action["capital"] = rightcapital
        position = 0
        for details in naija_states:
            position += 1
            print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")
    else: print("look the list well and type the numerical position of wetin you wan edit olodo")

elif inputt == "D":
    position = 0
    for details in naija_states:
        position += 1
        print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")
    delete_num = input("Enter the position of wetin you wan comot: \n")
    if delete_num.isnumeric:
        naija_states.pop(int(delete_num)-1)
        print("\nThe thing wey you delete don go\n")
        position = 0
        for details in naija_states:
            position += 1
            print(f"{position}. This is {details['state']} State and  {details['capital']} is its capital")

    

    