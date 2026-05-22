import streamlit as st
from emotion_detector import detect_emotion
from spotify_manager import get_spotify_playlists
import random
import time

# PAGE CONFIG

st.set_page_config(
    page_title="AuraTunes",
    page_icon="🎧",
    layout="wide"
)

# QUOTES

quotes = [
    "Every feeling deserves a soundtrack. 🎵",
    "Music understands emotions words cannot explain. ✨",
    "Your emotions create your rhythm. 🌌",
    "Turn your feelings into melodies. 💫",
    "Let your heart choose the music tonight. 🎧"
]

# CUSTOM CSS

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}
            
/* STARS */

.stApp::before {

    content: "✨ ✦ ✨ ✦ ✨";

    position: fixed;

    top: 40px;
    right: 40px;

    font-size: 24px;

    opacity: 0.15;

    animation: floatStars 6s ease-in-out infinite;
}

@keyframes floatStars {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0px);
    }
}            

/* TITLE */

.main-title {
    text-align: center;
    font-size: 85px;
    font-weight: 800;
    color: white;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* QUOTE */

.quote {
    text-align: center;
    font-size: 26px;
    color: #cbd5e1;
    margin-bottom: 35px;
    font-style: italic;
}

/* INPUTS */

.stTextInput input {

    background-color: rgba(255,255,255,0.08);
    color: white;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.12);
    padding: 14px;
    font-size: 16px;
}

.stTextArea textarea {

    background-color: rgba(255,255,255,0.08);
    color: white;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.12);
    padding: 18px;
    font-size: 16px;
}

.stSelectbox div[data-baseweb="select"] {

    background-color: rgba(255,255,255,0.08);
    border-radius: 14px;
}

/* BUTTON */

.stButton button {

    width: 100%;
    background: linear-gradient(90deg,#8b5cf6,#6366f1);
    color: white;
    border-radius: 14px;
    border: none;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {

    transform: scale(1.01);
}

/* EMOTION BOX */

.emotion-box {

    padding: 30px;
    border-radius: 24px;
    text-align: center;
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-top: 30px;
}

/* MESSAGE BOX */

.message-box {

    background: rgba(255,255,255,0.07);
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
    font-size: 18px;
    line-height: 1.8;
}

/* PLAYLIST CARD */

.playlist-card {

    background: rgba(255,255,255,0.07);
    padding: 22px;
    border-radius: 20px;
    margin-top: 16px;
    transition: 0.3s;
}

.playlist-card:hover {

    background: rgba(255,255,255,0.12);
}
            
/* ANIMATED BACKGROUND */

.stApp::before {

    content: "";

    position: fixed;

    top: -200px;
    left: -200px;

    width: 500px;
    height: 500px;

    background: #8b5cf6;

    opacity: 0.18;

    border-radius: 50%;

    filter: blur(120px);

    animation: float1 10s ease-in-out infinite;

    z-index: -1;
}

.stApp::after {

    content: "";

    position: fixed;

    bottom: -200px;
    right: -200px;

    width: 500px;
    height: 500px;

    background: #3b82f6;

    opacity: 0.18;

    border-radius: 50%;

    filter: blur(120px);

    animation: float2 12s ease-in-out infinite;

    z-index: -1;
}

@keyframes float1 {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-30px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes float2 {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(30px);
    }

    100% {
        transform: translateY(0px);
    }
}            

/* FOOTER */

.footer {

    text-align: center;
    margin-top: 60px;
    color: #94a3b8;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# TITLE

st.markdown(
    "<div class='main-title'>🎧 AuraTunes</div>",
    unsafe_allow_html=True
)

# QUOTE

st.markdown(
    f"<div class='quote'>{random.choice(quotes)}</div>",
    unsafe_allow_html=True
)

# MUSIC VISUALIZER

beat_col1, beat_col2, beat_col3, beat_col4, beat_col5 = st.columns(5)

with beat_col1:
    st.progress(30)

with beat_col2:
    st.progress(70)

with beat_col3:
    st.progress(100)

with beat_col4:
    st.progress(60)

with beat_col5:
    st.progress(85)

st.markdown("<br>", unsafe_allow_html=True)

# HERO SECTION

st.markdown("## 🌌 A quiet space for your emotions 🎧")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
🧠 AI Emotion Detection

AuraTunes gently understands emotions and transforms them into comforting music experiences.
"""
    )

with col2:
    st.info(
        """
🌍 Multilingual Soundtracks

Discover emotional playlists across Telugu, Hindi, Korean, Japanese and more.
"""
    )

with col3:
    st.info(
        """
🎧 Personalized Comfort

Every soundtrack is emotionally tailored to match your mood, energy and emotional space.
"""
    )

st.markdown("<br>", unsafe_allow_html=True)

# USER INPUTS

username = st.text_input(
    "🌌 Before we begin… what should I call you?"
)

user_mood = st.text_area(
    "🌙 Take a quiet moment for yourself...",
    height=220,
    placeholder="""
You don’t have to filter your feelings here.

Write about your day, your thoughts, what’s been heavy on your heart, 
or even the small emotions you’ve been carrying quietly.

AuraTunes is here to listen 🎧
"""
)

language = st.selectbox(
    "🌍 Choose the language your heart wants to hear",
    [
        "English",
        "Telugu",
        "Hindi",
        "Tamil",
        "Korean",
        "Japanese"
    ]
)

genre = st.selectbox(
    "🎵 What kind of comfort are you looking for tonight?",
    [
        "Melody",
        "Lo-fi",
        "Party",
        "Classical",
        "Indie",
        "Instrumental",
        "Rock"
    ]
)

# BUTTON
emotion = detect_emotion(user_mood)

# DYNAMIC THEMES

theme_colors = {

    "joy": "#facc15",
    "sadness": "#3b82f6",
    "anger": "#ef4444",
    "fear": "#a855f7",
    "neutral": "#64748b",
    "surprise": "#ec4899"
}

theme_color = theme_colors.get(
    emotion,
    "#8b5cf6"
)

st.markdown(
    f"""
    <style>

    .stApp {{

        background:
        radial-gradient(circle at top left,
        {theme_color}22,
        transparent 35%),

        radial-gradient(circle at bottom right,
        {theme_color}33,
        #020617 60%);
    }}

    </style>
    """,
    unsafe_allow_html=True
)
if st.button("🌌 Sit With My Feelings✨"):

    with st.spinner("🌌 AuraTunes is quietly listening to your emotions..."):

        time.sleep(2)

    emotion = detect_emotion(user_mood)


    # EMOTION STYLES

    emotion_styles = {

        "joy": ("#22c55e", "😊"),
        "sadness": ("#3b82f6", "💙"),
        "anger": ("#ef4444", "🔥"),
        "fear": ("#a855f7", "😨"),
        "neutral": ("#64748b", "✨"),
        "surprise": ("#f59e0b", "😲")
    }

    color, emoji = emotion_styles.get(
        emotion,
        ("#64748b", "✨")
    )

    # EMOTION BOX

    st.markdown(
        f"""
        <div class='emotion-box'
        style='background:linear-gradient(135deg,{color},#111827);'>
        {emoji} {emotion.upper()}
        </div>
        """,
        unsafe_allow_html=True
    )

    # EMOTIONAL REFLECTIONS

    emotion_messages = {

        "joy":
        "There’s warmth in your emotions today 🌞 Hold onto the little moments making your heart lighter.",

        "sadness":
        "It sounds like your heart has been carrying heaviness quietly for a while 💙 You don’t have to carry everything alone.",

        "anger":
        "Your emotions feel intense right now 🔥 Maybe tonight can simply be about breathing, slowing down and letting the noise soften.",

        "fear":
        "Something inside you seems overwhelmed 🌌 Let the music sit beside you gently for a while.",

        "neutral":
        "Not every emotion needs to be loud ☁️ Sometimes quiet feelings deserve attention too.",

        "surprise":
        "Life seems emotionally unexpected right now ✨ Give yourself a little grace while processing it all."
    }

    st.markdown(
        f"""
        <div class='message-box'>
        {emotion_messages.get(emotion)}
        </div>
        """,
        unsafe_allow_html=True
    )

    # PERSONALIZED MESSAGE

    personalized_messages = [

        f"{username}, these {language} {genre} soundtracks may gently resonate with your emotions tonight 🌌",

        f"These melodies were chosen to emotionally sit beside you tonight 🎧",

        f"{username}, maybe these songs can hold some of the feelings words couldn’t explain ✨",

        f"Sometimes music understands emotions more softly than conversations do 💫"
    ]

    st.markdown(
        f"""
        <div class='message-box'>
        {random.choice(personalized_messages)}
        </div>
        """,
        unsafe_allow_html=True
    )

    # PLAYLISTS

    playlists = get_spotify_playlists(
        emotion,
        language
    )

    st.subheader("🎶 A soundtrack for this moment")

    for playlist in playlists:

        st.markdown(
            f"""
            <div class='playlist-card'>

            <h4>🎧 {playlist['name']}</h4>

            <a href="{playlist['url']}" target="_blank">
            Open in Spotify →
            </a>

            </div>
            """,
            unsafe_allow_html=True
        )

# FOOTER

st.markdown(
    "<div class='footer'>Crafted with emotions, music & quiet moments ✨</div>",
    unsafe_allow_html=True
)