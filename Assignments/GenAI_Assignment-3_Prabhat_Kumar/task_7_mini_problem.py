def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

original_list = [100,200]

while True:
    print('Select Menu')
    print('1 for Add price')
    print('2 for Show average price')
    print('3 for Show highest price')
    print('q for Quit\n')

    action = input('Choose your menu\n')

    if action == '1':
        price = int(input("Enter price: "))
        add_price(original_list, price)
        print(original_list)

    elif action == '2':
        print('Average of price is ',get_average_price(original_list))

    elif action == '3':
        print('Max price is ',get_max_price(original_list))

    elif action == 'q':
        print('Exiting')
        break

    else:
        print("Invalid option")