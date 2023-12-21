class Product():

    def __init__(self,name , description, brand, model, price):
        self.name = name
        self.description = description
        self.brand = brand
        self.model = model
        self.price = price 
       

    def calculate_discount(self,discount=10):
        try:
            discountedprice = self.price * (discount/100)
        except TypeError:
            return 'Price is a number'
        except:
            return 'Error occured'
        return discountedprice
    
    def newprice(self):
        discount = self.calculate_discount()
        return self.price - discount

product1 = Product(
    name= "lexus",
    description= "sport car",
    brand= "toyota",
    model= "Rx350",
    price= 3500000
)

product2 = Product(
    name= "G-wagon",
    description= "Rich man car",
    brand= "mercedes benz",
    model= "2021",
    price= 35000000
)

product3 = Product(
    name= "camry",
    description= "comfy car",
    brand= "toyota",
    model= "xle",
    price= 2500000
   
)
# print(product1.price)
# print(product1.calculate_discount())
# print(product1.newprice())

def calc_all_prices(*args):
    allprice = 0
    for amount in args:
        allprice+=amount.newprice()  #also all_price = all_price +amount.new_price
    return allprice

print(calc_all_prices(product1,product2,product3))