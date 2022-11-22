
import pandas as pd
import streamlit as st
from database import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Customer Name','Customer ID','Customer Number','Gender'])
    with st.expander("View all Customers"):
        st.dataframe(df)