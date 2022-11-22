import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        C_name = st.text_input("Customer Name:")
        C_ID = st.text_input("Customer ID:")
        C_Phone_no = st.text_input("Customer Phone No:")
    with col2:
        C_gender = st.selectbox("Gender", ["Male", "Female",])
    if st.button("Add Customer"):
        add_data(C_name,C_ID,C_Phone_no,C_gender)
        st.success("Successfully added Customer: {}".format(C_name))