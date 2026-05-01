def process_prices(prices):
    disc_list = list(map(lambda price :price - (price * 10/100),prices))
    greater_300 = list(filter(lambda price:price>300,disc_list))

    return f'Discounted List -> {disc_list}\nGreater than 300 List -> {greater_300}'
    
    
    

print(process_prices([100,500,900,50,750]))
    