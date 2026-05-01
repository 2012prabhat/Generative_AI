
gst = lambda price:price+(0.18 * price)

print(gst(100))

# final amount after gst and discount 


final_amount = lambda price,disc:(price - (price * disc/100)) + (0.18 * price)

print(final_amount(1000,10))


