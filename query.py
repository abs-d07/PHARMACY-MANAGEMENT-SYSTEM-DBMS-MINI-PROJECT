import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, delete_data
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pms"
)
c = mydb.cursor()

def query():
    def sql_executor(raw_code):
        c.execute(raw_code)
        data = c.fetchall()
        return data
    
    train = ['Train_number','Train_name','Train_type','Train_source','Train_destination','Train_availability']
    buys_or_generates = ['C_ID','Dr_ID','I_No','Quantity']
    customer = ['C_Name','C_ID','C_Phone_no','C_Gender']
    distributor = ['D_Name','D_ID','D_Phone_no','D_Address']
    drug = ['Dr_Name','Dr_ID','Dr_DOM','Dr_DOE','Dr_MRP','Dr_Cost_Price','Dr_Type','Dr_Use','Dr_Quantity','D_ID','U_ID']
    invoice = ['I_Date','I_Time','I_Bill_Amount','I_No']
    user = ['U_Name','U_ID','U_DOB','U_Password','U_Phone_no','U_Address']

    st.title("MySQL Query Box ")
    #menu = ["Home","About"]
    #choice = st.sidebar.selectbox("Menu",menu)
    #if choice == "Home":
    st.subheader("Executing MySQL Queries")
        # Columns/Layout
    col1,col2 = st.columns(2)
    with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")
    with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)
                # Results 
                query_results = sql_executor(raw_code)
                #with st.expander("Results"):
                #    st.write(query_results)
                with st.expander("Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)
    #else:
    #    st.subheader("About")


