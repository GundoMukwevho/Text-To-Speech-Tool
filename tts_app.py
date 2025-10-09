import streamlit as st
import pyttsx3
from pathlib import Path

# Initialize TTS engine
engine = pyttsx3.init()

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Text-to-Speech Tool", page_icon="🎤")
st.title("🎤 Text-to-Speech Tool")
st.write("Type your text or upload a .txt file, choose voice, rate, volume, and click Speak!")

# Text input
text_input = st.text_area("Type your text here:")

# File upload
uploaded_file = st.file_uploader("Or upload a .txt file:", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

# Voice selection
voices = engine.getProperty("voices")
voice_names = [v.name for v in voices]
voice_choice = st.selectbox("Choose a voice:", voice_names)

# Rate and volume
rate = st.slider("Speech rate:", 100, 300, 150)
volume = st.slider("Volume:", 0.0, 1.0, 0.8)

# Speak button
if st.button("Speak"):
    if text_input.strip() == "":
        st.warning("Please enter text or upload a file!")
    else:
        engine.setProperty("voice", voices[voice_names.index(voice_choice)].id)
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)
        engine.say(text_input)
        engine.runAndWait()
        st.success("✅ Spoken successfully!")
