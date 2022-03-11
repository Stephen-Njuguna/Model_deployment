import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("neural_network.pkl","rb")
model = pickle.load(pickle_in)

def contraceptive_pred(site_code,product_code,stock_initial, stock_received, stock_adjustment, stock_end, average_monthly_consumption):
    prediction = model.predict([[site_code,product_code,stock_initial, stock_received, stock_adjustment, stock_end, average_monthly_consumption]])
    print(prediction)
    return prediction


def main():
    st.title("Contraceptive Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:whiite;text-align:center;"> cort de voir Contraceptive Stock Distribution ML App</h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    site_code = st.text_input("Site_Code")
    product_code = st.text_input("Product_Code")
    stock_initial = st.text_input("Stock_Initial")
    stock_received = st.text_input("Stock_Received")
    stock_adjustment = st.text_input("Stock_Adjustment")
    stock_end = st.text_input("Stock_End")
    average_monthly_consumption = st.text_input("Average_Monthly_Consumption")
    result = ""

    if st.button("Predict"):
        result = contraceptive_pred(site_code,product_code,stock_initial, stock_received, stock_adjustment, stock_end, average_monthly_consumption)
    st.success('The Stock Distribution is {}'.format(result))

if __name__ == '_main_':
    main()




