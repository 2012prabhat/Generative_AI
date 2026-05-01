# Task-1 Discount Rules (if/elif/else)

# write a program that reads an integer order_amount from the user using input()
try:
    order_amount = int(input("Enter order amount "))
    # apply the discount rules 
    discounted_amount = 0

    if order_amount>=2000:
        discount = 15
        discounted_amount = order_amount * discount/100
    elif order_amount>=1500:
        discount = 10
        discounted_amount = order_amount * discount/100
        
    elif order_amount>=1000:
        discount = 7
        discounted_amount = order_amount * discount/100
        
    else:
        discounted_amount = 0
        

    final_amount = order_amount - discounted_amount
    tax = (final_amount * 5/100)
    print('Subtotal ',final_amount)
    print('Tax ',tax)
    print('Final Total ',tax + final_amount)

except:
    print("Please enter a valid amount")
    





    

    
