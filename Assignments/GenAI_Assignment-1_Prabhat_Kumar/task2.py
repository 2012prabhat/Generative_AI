categories = ['Electronics','Sports','Books','Beauty','Clothing','Home']

# created categories set from categories list
categories_set = set(categories)

# i have added books in the categories set but it will already in the set so it wont added in the set.
categories_set.add('Books')
print(categories_set)

#check category exists or not in the category_set
result = 'Sports' in categories_set 
print(result)

#total number of unique categories using set
print(len(categories_set))