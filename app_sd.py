import streamlit as st
import speech_recognition as sr
from transformers import pipeline
import os
import tempfile

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")

def recognize_speech_from_audio_file(file_path):
    # Recognize speech using Google Web Speech API
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text_query = recognizer.recognize_google(audio_data)
            return text_query
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Streamlit app interface
st.title("ASR and Translation with Streamlit")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

if uploaded_file is not None:
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".audio") as tmp_audio:
        tmp_audio.write(uploaded_file.getbuffer())
        tmp_audio_path = tmp_audio.name

    st.write(f"Processing file: {uploaded_file.name}")

    # Recognize speech from audio file
    recognized_text = recognize_speech_from_audio_file(tmp_audio_path)
    st.write("Recognized Text:", recognized_text)

    # Translate recognized text
    if recognized_text and "Sorry" not in recognized_text:
        translated_text = translator(recognized_text)[0]['translation_text']
        st.write("Translated Text:", translated_text)

    # Clean up
    os.remove(tmp_audio_path)
