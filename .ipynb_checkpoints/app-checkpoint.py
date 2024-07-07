import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('language_detection_model.pckl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Ai")
input_test = st.text_input("Enter text to detect language", "amakuru yawe")

button_clicked = st.button("Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))
st.markdown("---")
st.markdown("Created by [ProgrammerDATCH](https://programmerdatch.netlify.app)", unsafe_allow_html=True)