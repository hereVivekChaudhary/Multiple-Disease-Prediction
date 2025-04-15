# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:16:37 2024

@author: Rahul Thakur
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model=pickle.load(open('C:/Users/MCC SOLUTION NUH/Desktop/Multiple Disease Prediction Project/Saved Models/heart_disease_model.sav', 'rb'))

heart_disease_model=pickle.load(open('C:/Users/MCC SOLUTION NUH/Desktop/Multiple Disease Prediction Project/Saved Models/heart_disease_model.sav', 'rb'))

parkinsons_model=pickle.load(open('C:/Users/MCC SOLUTION NUH/Desktop/Multiple Disease Prediction Project/Saved Models/parkinsons_model.sav', 'rb'))


#sidebar to navigate

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)


#Diabetes prediction page
if(selected== 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('Blood pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetsPedigreeFunction=st.text_input('Diabetes Pedigree function value')
    with col2:
        Age=st.text_input('Age of the Person')
    
    #code for prediction
    diab_diagnosis=''
    
    #code for button
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetsPedigreeFunction,Age]])
        
        if(diab_prediction[0]==0):
            diab_diagnosis='The Person is Not Diabetic'
        else:
            diab_diagnosis='The Person is  Diabetic'
    st.success(diab_diagnosis)

#Heart disease prediction page
if(selected== 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    #getting the input from the users
    with col1:
        age=st.text_input('Enter Your Age')
    with col2:
        sex=st.text_input('Enter Sex: 0 for male , 1 for female')
    with col3:
        cp=st.text_input('Enter Chest pain type 0-3')
    with col1:
        trestbps=st.text_input('Resting blood pressure between 90-200')
    with col2:
        chol=st.text_input('Enter Your cholestrol value between 100-400   ')
    with col3:
        fbs=st.text_input('Enter Your fasting blood pressure from 0 to 1')
    with col1:
        restecg=st.text_input('Enter Your electrocardiographic result from 0 to 1')
    with col2:
        thalach=st.text_input('Enter Your Maximum heart rate between 90-200')
    with col3:
        exang=st.text_input('Enter Your exercise induced Angina from 0-1')
    with col1:
        oldpeak=st.text_input('Enter Your ST depression induced by exercise relative to rest from 0-5.0')
    with col2:
        slope=st.text_input('Enter the slope of the peak exercise ST segment from 0-2')
    with col3:
        ca=st.text_input('Enter  number of major vessels (0-3) colored by fluoroscopy from 0-4')
    with col1:
        thal=st.text_input('Enter  [normal; fixed defect; reversible defect from 1-3]')
    
    #code for prediction
    heart_diagnosis=''
    
    #creating a button for prediction
    if st.button('Heart Disease Prediction Result'):
         heart_diagnosis=heart_disease_model.predict([age,sex,cp ,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
         if(heart_diagnosis[0]==0):
             diab_diagnosis='The Person does not have a Heart Disease'
         else:
             diab_diagnosis='The Person has a Heart Disease'
         
    st.success(heart_diagnosis)


#Parkinsons prediction page
if(selected== 'Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter=st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        MDVP_RAP=st.text_input('MDVP:RAP')
    with col2:
        MDVP_PPQ=st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP=st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer=st.text_input(' MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_dB=st.text_input(' MDVP:Shimmer(dB)')
    with col1:
        Shimmer_APQ3=st.text_input(' Shimmer:APQ3')
    with col2:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        status=st.text_input('status')
    with col3:
        RPDE=st.text_input('RPDE')
    with col4:
        DFA=st.text_input('DFA')
    with col5:
        spread1=st.text_input('spread1')
    with col1:
        spread2=st.text_input('spread2')
    with col2:
        D2=st.text_input('D2')
    with col3:
        PPE=st.text_input('PPE')
    
    #code for prediction
    parkinsons_diagnosis=''
    
    #creating a button for prediction
    if st.button('Parkinsons Prediction Result'):
         parkinsons_prediction=parkinsons_model.predict([fo,Fhi,Flo ,jitter_percent,Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR, status,RPDE, DFA,spread1,spread2,D2,PPE])
         if(parkinsons_prediction[0]==0):
             parkinsons_diagnosis='The Person does not have a Parkinsons Disease'
         else:
             parkinsons_diagnosis='The Person has a Parkinsons Disease'
         
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    