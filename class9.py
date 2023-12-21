list1 = ["bad","poor", "evil","terrible","wicked",]
list2 = ["good","very good", "excellent","intelligent", "brilliant"]
newlist = []
"""def odd():
    for x in list1:
        length = len(list1)
        if length %/"""
def sortlist(item1,item2):
    if type(item1) != list or type(item2) !=list:
        print("the first parameter is not a list")
    else:
        for eachitem in list1:
            indexx = list1.index(eachitem)
            # print(eachitem, "-", indexx)
            if indexx % 2 ==1:
                newlist.append(eachitem)
                
        
        """for eachitem in list2:
            if list2.index(eachitem)%2 ==0:
                print("the position is even", list(eachitem))
                print(eachitem)
                newlist.append(eachitem)"""
        
        for eachitem in list2:
            indexx = list2.index(eachitem)
            # print(eachitem, "-", indexx)
            if indexx%2 ==0:
                newlist.append(eachitem)
    return newlist
(sortlist(list1,list2))
def loopalist(list):
    try:
        for item in list:
            print(item)
    except: 
        print('invalid arg')
loopalist(newlist)
collectinfo = input("enter a number: ")

try:
    result = int(collectinfo) / 2
    print(result)
    print("olawale")

except NameError:
    print("does not exist")
except ValueError:
    print("the value you entered can not be processed")
except:
    print("error occurred")
else:
    print("try block successfully executed")
finally:
    print("this is the end of the try block")








