# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:16:55 2023

@author: Annyjerry
"""


import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color: red; padding: 15px;">
        <h2  style="color: white;text-align: center;"> Heart Disease Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html =True)
    
    model = joblib.load(r'C:\Users\Annyjerry\Desktop\JUSTICE FILES\python project\marchine learning Projects\heart Disease\heart disease algorithm')
    p1 = st.number_input('enter your Age')  
    s1 = st.selectbox('sex',('male','female'))
    if s1 == 'male':
        p2 = 1
    else:
        p2 = 0
    p3 = st.slider('cp',0,1)
    p4 = st.number_input('enter your Value trestbps(your resting blood pressure)')
    p5 = st.number_input('value of cholesterol')
    p6 = st.slider('enter your Value fbs(fasting blood sugar)',0,1)
    p7 = st.slider('enter your value of restecg(Resting electrocardiographic measurement)',0,1)
    p8 = st.number_input('value of thalac(maximum heart rate)')
    p9 = st.slider('enter your Value exang(the exercise induced angina)',0,1)
    p10 = st.number_input('value of oldpeak(ST depression induced by exercise relative to rest)')
    p11 = st.slider('enter your Value slope',0,3)
    p12 = st.slider('enter your Value ca(calcium)',0,3)
    p13 = st.slider('enter your Value thal(thalassemia)',0,3 )
    
    
    if st.button('predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]])
        if pred == 0:
            pred = 'your heart is safe'
            st.success(pred)
        else:
            pred = 'please meet the doctor your Heart is unsafe'
            
            st.success(pred)
        
    
    
     

if __name__ == '__main__':
    main()