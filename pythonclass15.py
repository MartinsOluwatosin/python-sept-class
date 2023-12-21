class Student():
    
    def __init__(self, firstname, lastname, age, phn_num, DOB ):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.phn_num = phn_num
      self.DOB = DOB 

def returnEmail(self):
    return f'{self.firstname.lower()}-{self.lastname.lower()}@parachict.com'



def changeDate(self):
    
    day = self.DOB.split('-')[0]
    mon = self.DOB.split('-')[1]
    year = self.DOB.split('-')[2]

    # Remove 0 on the days
    if day.startswith('0'):
        day = day[1:]

    # Remove 0 on the months
    if mon.startswith('0'):
        mon = mon[1:]

    # Putting position on day
    if day.endswith('11') or day.endswith('12') or day.endswith('13'):
        day += 'th'
    elif day.endswith('1'):
        day += 'st'
    elif day.endswith('2'):
        day += 'nd'
    elif day.endswith('3'):
        day += 'rd'
    else:
        day += 'th'

    mon_short_word = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    mon_Sht = mon_short_word[int(mon)-1]
        
    
    print(f'{day}-{mon_Sht}-{year}')
    return f'{day}-{mon_Sht}-{year}'




student1 = Student(
    firstname= "Irah",
    lastname= "Ayra",
    age= 22,
    phn_num= "07062528687",
    DOB= "22-06-2001"
)

student2 = Student(
    firstname= "Joshua",
    lastname= "Parach",
    age= 27,
    phn_num= "07082558987",
    DOB= "29-09-1996"
)
print(student1.firstname)
print(student1.changeDate())
print(student1.returnEmail())
print(student2.returnEmail())

""" create a product object
name , description, brand, model, price, return discount

calculate the total number of all object price after removing discount"""
