import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, get_customer, edit_Customer_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Customer_Name','Customer_ID','Customer_Number','Gender'])
    with st.expander("Current Customers"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Customer to Edit", list_of_customers)
    selected_result = get_customer(selected_customer)
    if selected_result:
        #Customer_Name = selected_result[0][0]
        #Customer_ID = selected_result[0][1]
        #Customer_Number= selected_result[0][2]
        #Gender= selected_result[0][3]
        #gender_list = ["Male", "Female"]
        C_Name = selected_result[0][0]
        C_ID = selected_result[0][1]
        C_Phone_no= selected_result[0][2]
        C_Gender= selected_result[0][3]
        gender_list = ["Male", "Female"]

        col1, col2 = st.columns(2)
        with col1:
            new_C_Name = st.text_input("Name:",C_Name)
            new_C_ID = st.text_input("ID:", C_ID)
            new_C_Phone_no = st.text_input("Number:", C_Phone_no)
        with col2:
            new_C_Gender = st.selectbox("Gender", ["Male", "Female"])
        if st.button("Update Customer"):
            #edit_Customer_data(new_C_name,new_C_ID,new_C_Phone_no,new_gender,Customer_Name,#Customer_ID,Customer_Number,Gender)
            edit_Customer_data(new_C_Name,new_C_ID,new_C_Phone_no,new_C_Gender,C_Name, C_ID, C_Phone_no, C_Gender)
            #st.success("Successfully updated: {} to : {}".format(C_Name,new_C_Name))
            st.success("Successfully updated: {}".format(new_C_Name))
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Customer_Name','Customer_ID','Customer_Number','Gender'])
    with st.expander("Updated data"):
        st.dataframe(df2)
    