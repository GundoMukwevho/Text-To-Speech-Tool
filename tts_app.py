import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

st.set_page_config(page_title="Text-to-Speech Tool", page_icon="🎤")
st.title("🎤 Text-to-Speech Tool")
st.write("Type your text or upload a .txt file, then press Speak!")

# Text input
text_input = st.text_area("Type your text here:")

# File upload
uploaded_file = st.file_uploader("Or upload a .txt file:", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

# Language selection (optional)
language = st.selectbox("Choose language:", ["en", "es", "fr"], index=0)

# Speak button
if st.button("Speak"):
    if text_input.strip() == "":
        st.warning("Please enter text or upload a file!")
    else:
        # Generate TTS
        tts = gTTS(text=text_input, lang=language)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Play audio in Streamlit
        st.audio(mp3_fp, format="audio/mp3")
        st.success("✅ Spoken successfully!")
