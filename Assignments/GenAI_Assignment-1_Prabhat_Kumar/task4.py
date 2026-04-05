
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

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print('Category Products',category_to_products)


# print all products that belong to the category that has maximum number of products
maxProductsLen = 0
for category,products in category_to_products.items():
    print(category)
    if len(products) > maxProductsLen:
        maxProducts = products
        maxProductsLen = len(products)
        
for elem in maxProducts:
    print(elem)
