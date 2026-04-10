import streamlit as st
st.title("Hello from Streamlit")
st.write('Hello')
st.header("Welcome to streamlit")
# st.button("Click me")

if st.button("Click me"):
    st.write("Button is clicked")
    
agree = st.checkbox('I agree')
if agree:
    st.write('You are agreed !')
    
st.slider("Select value",1, 10, 8)


