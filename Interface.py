import numpy as np
import pickle
import streamlit as st
from PIL import Image

loaded_model = pickle.load(open("https:/github.com/jazidesigns/streamlit/blob/main/voting_classifier.sav", "rb"))

def risk_prediction(input_data):
    prediction = loaded_model.predict(input_data)
    if prediction[0] == "low risk":
        return "Low Maternal Health Risk"
    elif prediction[0] == "mid risk":
        return "Medium Maternal Health Risk"
    else:
        return "High Maternal Health Risk"

    print(prediction)
    
def main():
    
    Age = st.text_input("Age")
    SystolicBP = st.text_input("Systolic Blood Pressure")
    DiastolicBP = st.text_input("Diastolic Blood Pressure")
    BS = st.text_input("Blood Sugar")
    BodyTemp = st.text_input("Body Temperature")
    HeartRate = st.text_input("Heart Rate")
    
    
    prediction = ""
    
    if st.button("Prediction"):
        prediction = risk_prediction([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])
    
    st.success(prediction)

st.title("Maternal Health Risk Prediction")
img = Image.open("https:/github.com/jazidesigns/streamlit/blob/main/maternal-health.png")
st.image(img)    

if __name__ == "__main__":
    main()
