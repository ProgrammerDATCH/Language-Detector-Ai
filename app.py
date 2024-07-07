import pickle
import string
import streamlit as st
import webbrowser
import os

st.title("Language Detection AI")

global Lrdetect_Model

# Check if the file exists
if os.path.exists('language_detection_model.pckl'):
    with open('language_detection_model.pckl', 'rb') as LrdetectFile:
        try:
            Lrdetect_Model = pickle.load(LrdetectFile)
        except Exception as e:
            st.error(f"Error loading model: {e}")
else:
    st.error("File not found: language_detection_model.pckl")

input_test = st.text_input("Enter text to detect language", "amakuru yawe")

button_clicked = st.button("Get Language Name")
if button_clicked:
    try:
        prediction = Lrdetect_Model.predict([input_test])
        st.text(prediction)
    except Exception as e:
        st.error(f"Error making prediction: {e}")

st.markdown("---")
st.markdown("Created by [ProgrammerDATCH](https://programmerdatch.netlify.app)", unsafe_allow_html=True)