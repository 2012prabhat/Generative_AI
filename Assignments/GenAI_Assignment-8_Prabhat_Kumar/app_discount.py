import streamlit as st

product_price = st.number_input("Enter Product Price")
discount_percentage = st.slider('Select Discount Percentage',0,50)

if st.button('Calculate Discounted Price'):
    disc_price = product_price * (discount_percentage/100)
    st.success(product_price - disc_price)
    
# comparison table between after or before price
    table_data = {
    "Time":["Before","After"],
    "Price":[product_price,product_price-disc_price]
    }
    st.table(table_data)
    

    