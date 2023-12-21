import classassignment

allprice = classassignment.calc_all_prices
productclass = classassignment.Product

product4 = productclass("brabus","foreign","benz", 2023, 2300000)
product5 = productclass("pickup","foreign","toyota", "hilux", 300000)

print(product4.price)
print(product4.newprice())

print(allprice(product4,product5))