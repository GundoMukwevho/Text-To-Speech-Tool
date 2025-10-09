import streamlit as st
from gtts import gTTS
from io import BytesIO

# ----------------- Page config -----------------
st.set_page_config(
    page_title="Text-to-Speech Tool 🎤",
    page_icon="🎤",
    layout="centered",
)

# ----------------- Custom CSS -----------------
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background-color: #f0f8ff;
    }
    /* Buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    /* Text areas */
    textarea {
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    /* Headers */
    h1, h2, h3 {
        color: #1E90FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- App Title -----------------
st.title("🎤 Text-to-Speech Tool")
st.subheader("Type, or paste text or upload a file, select your preferred language, and click Speak!")

# ----------------- Layout -----------------
col1, col2 = st.columns([3, 1])

with col1:
    text_input = st.text_area("Type your text here:")

    uploaded_file = st.file_uploader("Or upload a .txt file:", type=["txt"])
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode("utf-8")

with col2:
    st.markdown("### ⚙️ Settings")
    language = st.selectbox("Language:", ["en", "es", "fr"], index=0)

# ----------------- Speak Button -----------------
if st.button("Speak 🔊"):
    if not text_input.strip():
        st.warning("Please enter text or upload a file!")
    else:
        # Generate TTS
        tts = gTTS(text=text_input, lang=language)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Play audio
        st.audio(mp3_fp, format="audio/mp3")
        st.success("✅ Spoken successfully!")

