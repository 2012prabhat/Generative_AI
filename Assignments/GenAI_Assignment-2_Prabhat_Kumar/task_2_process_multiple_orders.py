orders = [1200,2500,800,1750,3000]

#total of final revenue of orders
total_revenue = 0

# elements which receives discount
disc_orders = 0

for idx,elem in enumerate(orders):
    disc = 0
    if elem>=2000:
        disc = 15
    elif elem>=1500:
        disc = 10
    elif elem>=1000:
        disc = 7
    else:
        disc = 0
    if disc>0:
        disc_orders = disc_orders+1
    final_amount = elem - (elem * disc/100)
    total_revenue = total_revenue + final_amount

    print(f'Order Amount -> {elem},  Discount % -> {disc}%,  Final Amount -> {final_amount}')
    
print('Total Revenue', total_revenue)

print('Orders which get discount',disc_orders)