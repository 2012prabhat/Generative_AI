prices = [100,250,400,1200,50]
gst = lambda price:price+(0.18 * price)

new_prices = list(map(gst,prices))


print('Original Prices',prices)
print('Prices After GST',new_prices)