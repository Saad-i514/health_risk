import pickle
import numpy as np
import streamlit as st

load_model=pickle.load(open("xgb_model.pkl","rb"))

def predict(features):
    X=np.array([features])
    return load_model.predict(X)[0]

st.title("Risk Predictor")
age=st.number_input("age",min_value=0,step=1,value=30)
weight=st.number_input("weight",min_value=0,step=1,value=70)
height=st.number_input("height",min_value=0,step=1,value=170)
exercise=st.number_input("exercise",min_value=0,step=1,value=1)
sleep=st.number_input("sleep",min_value=0,step=1,value=7)
sugar_intake=st.number_input("sugar intake",min_value=0,step=1,value=1)
bmi_recalc=st.number_input("bmi_recalc",min_value=0.0,step=0.1,value=22.5)
smoking_yes=st.selectbox("smoking_yes",[0,1],index=0)
alcohol_yes=st.selectbox("alcohol_yes",[0,1],index=0)
profession_doctor=st.selectbox("profession_doctor",[0,1],index=0)
profession_driver=st.selectbox("profession_driver",[0,1],index=0)
profession_engineer=st.selectbox("profession_engineer",[0,1],index=0)
profession_farmer=st.selectbox("profession_farmer",[0,1],index=0)
profession_office_worker=st.selectbox("profession_office_worker",[0,1],index=0)
profession_student=st.selectbox("profession_student",[0,1],index=0)
profession_teacher=st.selectbox("profession_teacher",[0,1],index=0)

if st.button("Predict"):
    features=[int(age),int(weight),int(height),int(exercise),int(sleep),int(sugar_intake),float(bmi_recalc),int(smoking_yes),int(alcohol_yes),int(profession_doctor),int(profession_driver),int(profession_engineer),int(profession_farmer),int(profession_office_worker),int(profession_student),int(profession_teacher)]
    pred=predict(features)
    if pred==1:
        st.error("High Risk")
    else:
        st.success("Save")
 
