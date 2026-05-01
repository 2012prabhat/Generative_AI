def apply_discount(price,discount_percent=5):
    if discount_percent>60:
        return 'Discount should not be more than 60% '
    return price - (price * discount_percent/100)

print(apply_discount(100,10)) 
print(apply_discount(500,61))

   