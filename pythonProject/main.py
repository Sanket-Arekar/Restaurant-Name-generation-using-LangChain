import streamlit as st
from langchain_helper import generate_restaurant_names_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian","Arabic","Mexican","American","Italian"))


if cuisine:
    response = generate_restaurant_names_and_items(cuisine)
    st.header(response['restaurant'])
    menu_items = response['menu_items'].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

