import streamlit as st 
import numpy as np 
import pandas as pd 
import joblib

st.title("Car price prediction App")
st.header('Enter infomation below ')

user_input1 = st.text_input('car_name & model')
user_iput2 = st.slider('Age',0,20)
user_input3 = st.number_input('KM_driven',0,150000)
user_input4 = st.text_input('Transmition type')
user_input5 = st.selectbox('choose engine type',[800,1200,1400,1600,1800,2000])
user_input6 = st.number_input('Mximum power',40,150)

predict_clicked = st.button('Get prediction')

if predict_clicked == True:
    model = joblib.load('Random_forest.pkl')

    # Load data into numpy array:
    data = pd.DataFrame({
        'car_name':[user_input1],
        'vehicle_age':[user_iput2],
        'km_driven':[user_input3],
        'transmission_type':[user_input4],
        'engine':[user_input5],
        'max_power':[user_input6]

    })

    # Call model to predict:
    results = model.predict(data)

    st.success(f'The price of the car is {results[0]}')






