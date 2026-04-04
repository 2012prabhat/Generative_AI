#create a product price dictionay
price_dict = {
    'mobile':10000,
    'television':30000,
    'shoes':1000,
    'tablet':20000,
    'mouse':500,
    'laptop':50000
}

# Add new product in the price dictionary
price_dict['bike'] = 100000
price_dict['shoes'] = 1500
if 'tablet1' in price_dict:
    price_dict.pop('tablet1')
print(price_dict)


#print the average of price
total = 0
for val in price_dict:
    total += price_dict[val]
average = total/len(price_dict)
print(average)

#print the product with minimum and maximum price
minPrice = min(price_dict.values())
maxPrice = max(price_dict.values())
for key,value in price_dict.items():
    if value == minPrice:
        minPricePro = key
    if value == maxPrice:
        maxPricePro = key

print('Product with Minimum Price',minPricePro)
print('Product with Maximum Price',maxPricePro)

#other way to do so 
minProd = min(price_dict,key=price_dict.get)
maxProd = max(price_dict,key=price_dict.get)

print(minProd)
print(maxProd)



