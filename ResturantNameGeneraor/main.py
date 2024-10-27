import streamlit as st
import langchain_helper

st.title("restaurant name generator")


cuisine = st.sidebar.selectbox("pick a cuisine ", ("indian", "italian", "mexican"))

if cuisine:
    response = langchain_helper.genearte_restro_menu(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_itm = response["menu_items"].strip().split(",")
    st.write("****Menu Items****")
    for item in menu_itm:
        st.write("", item)
