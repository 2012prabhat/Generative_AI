prices = [100,250,400,1200,50,2000,850]

prices_greater = list(filter(lambda price:price>500,prices))

prices_lesser = list(filter(lambda price:price<=500,prices))

print("Prices Greater than 500",prices_greater)
print("Prices Lesser than or equal to 500",prices_lesser)