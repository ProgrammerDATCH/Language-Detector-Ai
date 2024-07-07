import pickle
import string
import streamlit as st
import webbrowser
import os

st.set_page_config(page_title="Language detector", page_icon="🌐", menu_items={'Get Help': 'https://programmerdatch.netlify.app'})

st.title("Language Detection Ai")

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

st.markdown('''
            Based on NLP, this Ai can detect language you wrote among 4 languages used in Rwanda:
            (Kinyarwanda, English, French and Kiswahili).
            ''')

st.markdown("---")

input_test = st.text_input("Enter text to detect language", placeholder="Enter text here...")

button_clicked = st.button("Get Language Name", use_container_width=True)
if button_clicked:
    try:
        if input_test:
            prediction = Lrdetect_Model.predict([input_test])
            st.markdown(
                f'''
                <h1 style="text-align: center; color: green;">{prediction[0]}</h1>
                ''',
                unsafe_allow_html=True)
        else:
            st.markdown("<div style='width: 100%; text-align: center;'>Enter text please!</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error making prediction: {e}")

st.markdown("---")
st.markdown("Created by [ProgrammerDATCH](https://programmerdatch.netlify.app)", unsafe_allow_html=True)