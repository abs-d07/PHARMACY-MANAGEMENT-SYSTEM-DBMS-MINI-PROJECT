import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Customer Name','Customer ID','Customer Number','Gender'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_Customer = st.selectbox("Task to Delete", list_of_customers)
    st.warning("Do you want to delete :{}".format(selected_Customer))
    if st.button("Delete Customer"):
        delete_data(selected_Customer)
        st.success("Customer has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Customer Name','Customer ID','Customer Number','Gender'])
    with st.expander("Updated data"):
        st.dataframe(df2)