import streamlit as st

# title
st.title('Mini Dashboard')
st.subheader('Simple Sales Dashboard')
months = ['January','February','March','April']
selected_month = st.selectbox('Select Months',months)
sales = {
    "January":1200,
    "February":1500,
    "March":900,
    "April":2000
}

# Show only selected month sales
st.metric(label=f"Sales for {selected_month}", value=sales[selected_month])

#display a bar chart 
st.bar_chart(list(sales.values()))


