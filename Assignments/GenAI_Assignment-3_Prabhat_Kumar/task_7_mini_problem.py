def add_price(prices_list,price):
    return prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list)/len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

print(get_average_price([100,200]))
print(get_max_price([100,200,450,670]))