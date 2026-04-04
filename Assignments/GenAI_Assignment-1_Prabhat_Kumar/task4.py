
#1 create a list of tuples named catelog where each tuple is (product_name,price,category)

products = ['mobile','television','shoes','laptop','tablet','mouse']
categories = ['Electronics','Electronics','Clothing','Electronics','Electronics','Electronics']
price_dict = {
    'mobile':10000,
    'television':30000,
    'shoes':1000,
    'tablet':20000,
    'mouse':500,
    'laptop':50000
}

catalog = []

for idx, val in enumerate(products):
    prodTuple = (val,price_dict[val],categories[idx])
    catalog.append(prodTuple)

print(catalog)


#2 from catalog, create new dictionary category_to_products that maps each category to a list of product names in that category
category_to_products = {}
for product,price,category in catalog:
    category_to_products[category] = []

print('Category Products',category_to_products)