
daily = [200,150,0,400,50,-1,300]
total_sales = 0
corrupData = False

for idx, day in enumerate(daily):
    if day == -1:
        corrupData = True
        break
    elif day==0:
        continue
    else:
        total_sales = day + total_sales
        
if corrupData==False:
    print('Final Total',total_sales)
        
    
        
        
