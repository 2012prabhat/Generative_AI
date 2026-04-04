#1 create list named product
products = ['mobile','television','shoes','laptop','tablet','mouse']

#2 create a tuple named sample_product
sample_product = ('laptop',30000,'electronics')

#3 print second product
print(products[1])

#4 print last product
print(products[len(products)-1])

#5 Append two new product and then print it
products.append("keyboard")
products.append("headphone")
print(products)

#6 convert sample_product into list and change its price and convert back to tuple
sample_product = list(sample_product)
sample_product[1] = 5000
sample_product = tuple(sample_product)
print(sample_product)



