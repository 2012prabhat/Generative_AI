import streamlit as st

# title for sidebar
st.sidebar.title("Product Form")

#product name
product_name = st.sidebar.text_input("Product Name")

#product category
product_category = st.sidebar.selectbox(
    "Please select your product category",
    ("Electronics", "Sports", "Books","Fitness","Beauty"),
)

#product price
product_price = st.sidebar.number_input("Price")

#when user click add product button show a success message with products details 

if st.sidebar.button("Add Product"):
    st.success("Product added successfully")
    st.write("Added product details:-")
    st.write(f'Product name is {product_name}')
    st.write(f'Product category is {product_category}')
    st.write(f'Product price is {product_price}')
