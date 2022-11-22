import streamlit as st
from create import create
from delete import delete
from read import read
from update import update
import pandas as pd
import datetime
from database import view_all_data, view_only_customer_names, get_customer, edit_Customer_data,delete_data,add_data,create_table
from database import *

'''
    if st.button("Add Train"):
        add_data(Train_number, Train_name, Train_type, Train_source, Train_destination,Train_availability)
        st.success("Successfully added Train: {}".format(Train_number))

'''
def invoice():
    #print("issue")
    cola,colb = st.columns(2)
    #cola, colb = st.columns(2)
    with cola:
        I_Date = st.text_input("Invoice Date")
        I_Time = st.text_input("Invoice Time")
        I_No = st.text_input("Invoice Number")
    if st.button("Create Ivoice"):
            add_data_inv(I_Date,I_Time,I_No)
            st.success("Successfully Created invoice : {}".format(I_No))
    '''
    with colb:
        C_ID = st.text_input("Customer ID")
        Dr_ID = st.text_input("Drug ID")
        I_No = st.text_input("Invoice No")
        Quantity = st.text_input("Quantity")

    if st.button("Issue Medicine"):
            add_data_bog(C_ID,Dr_ID,I_No,Quantity)
            st.success("Successfully Issued {} to {}".format(Dr_ID,C_ID))
    '''

