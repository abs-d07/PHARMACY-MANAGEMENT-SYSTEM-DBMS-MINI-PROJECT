# Importing pakages
import streamlit as st
import mysql.connector
import pandas as pd
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from query import query
from issue import issue
from invoice import invoice
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():

        st.title("PHARMACY MANAGEMENT SYSTEM")
        #menu = ["Home","Create", "Read", "Update", "Delete","Query"]
        #menu = ["Home","Create", "Read", "Update", "Delete","Query","Create Invoice"]
        menu = ["Home","Create", "Read", "Update", "Delete","Query","Create Invoice","Issue medicine"]
        choice = st.sidebar.selectbox("Menu", menu)

        create_table()
        if choice == "Home":
            st.subheader("DBMS MINI PROJECT")
            set_background('C:/Users/abbub/Desktop/images.jpg')
            
            st.subheader("Project Abstract:")
            st.subheader("->The aim of building Pharmacy Management System was to digitalize the work of pharmacist.")
            st.subheader("->It helps them in maintaining records of drugs, distributors and customers.")
            st.subheader("->It's features aids in resolution of challenges with manual pharmacy management.")
            st.subheader("->It oversees and manages the pharmacy team to preserve strong working relationships and outcomes.")
            st.subheader("->This can also improve quality and customer satisfaction ratings, as well as keep medicines from going bad.")


        if choice == "Create":
            st.subheader("Enter Customer Details:")
            create()

        elif choice == "Read":
            st.subheader("View Customer table")
            read()

        elif choice == "Update":
            st.subheader("Update Customer table")
            update()

        elif choice == "Delete":
            st.subheader("Delete Customer table")
            delete()
        elif choice == "Query":
            st.subheader("Executing few queries")
            query()
        elif choice == "Create Invoice":
            st.subheader("Issuing Medicine to customer")
            invoice()
        elif choice == "Issue medicine":
            st.subheader("Issuing Medicine to customer")
            issue()

        #else:
        #   st.subheader("About PMS")


if __name__ == '__main__':
   main()
