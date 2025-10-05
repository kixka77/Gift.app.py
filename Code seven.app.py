# app.py
# Pages for Nay - Scrapbook Streamlit app (improved: book frame, centered secret button, flip animation)
# Run: pip install streamlit
#      streamlit run app.py

import streamlit as st
from pathlib import Path
from textwrap import dedent

st.set_page_config(page_title="Pages for Nay🩷", page_icon="💌", layout="centered")

# If you hosted an mp3, change this URL
AUDIO_SRC = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# CSS (do NOT use f-string here; keep as plain string)
STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Nunito:wght@300;400;700&display=swap');

:root{
  --bg1: #ff6fa3;  /* vivid pink */
  --bg2: #9b6ad6;  /* vivid purple */
  --accent: #ffd6ea;
  --paper: #fffaf8;
  --text: #3b2740;
}

/* page background */
html, body, [class*="css"] {
  background: linear-gradient(160deg, var(--bg1), var(--bg2)) fixed;
  color: var(--text);
  font-family: Nunito, "Segoe UI", sans-serif;
}

/* app container centers the book */
.app-wrap {
  max-width: 820px;
  margin: 18px auto;
  padding: 12px;
}

/* book frame (scrapbook look) */
.book-frame {
  background: linear-gradient(180deg, rgba(255,255,255,0.98), var(--paper));
  border-radius: 20px;
  padding: 26px;
  box-shadow: 0 20px 40px rgba(86, 30, 97, 0.18), inset 0 1px 0 rgba(255,255,255,0.7);
  border: 3px solid rgba(155,106,214,0.12);
  position: relative;
  overflow: hidden;
  margin: 8px;
}

/* cursive title */
.title {
  font-family: 'Great Vibes', cursive;
  font-size: 36px;
  color: #5b2b5d;
  margin-bottom: 6px;
  text-align: center;
}

/* subtitle */
.subtitle {
  text-align: center;
  color: #7b4f7b;
  margin-bottom: 12px;
}

/* page body card (where text goes) */
.page-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.995), rgba(255,250,252,0.995));
  padding: 18px;
  border-radius: 12px;
  box-shadow: 0 8px 22px rgba(120,60,120,0.06);
  display: flex;
  gap: 18px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  animation: flipIn 0.6s ease;
}

/* flip animation */
@keyframes flipIn {
  0%   { transform: rotateY(-90deg) translateY(8px); opacity: 0; }
  60%  { transform: rotateY(10deg) translateY(0); opacity: 0.95; }
  100% { transform: rotateY(0deg) translateY(0); opacity: 1; }
}

/* image box fallback */
.image-box {
  width: 220px;
  height: 170px;
  border-radius: 10px;
  background: linear-gradient(180deg,#fff0f6,#fff7fb);
  display:flex;
  align-items:center;
  justify-content:center;
  border: 1px dashed rgba(140,80,120,0.12);
  color: rgba(100,60,90,0.9);
  font-size: 14px;
}

/* text column */
.text-col {
  max-width: 380px;
  color: #3b2740;
  line-height: 1.55;
  font-size: 15px;
  text-align: left;
}

/* nav row - centered */
.nav-row {
  display:flex;
  gap:16px;
  justify-content:center;
  align-items:center;
  margin-top: 16px;
}

/* style Streamlit buttons (targets the generated button element) */
.stButton>button {
  background: linear-gradient(90deg,#9b6ad6,#ff8fb3);
  color: white;
  padding: 10px 18px;
  border-radius: 12px;
  border: none;
  font-weight: 600;
  box-shadow: 0 12px 28px rgba(150,70,150,0.12);
  cursor: pointer;
}

/* small hint text */
.hint {
  color: #7b4f7b;
  font-size: 0.95rem;
  text-align: center;
  margin-top: 8px;
}

/* sparkles overlay */
.sparkles {
  position:absolute;
  left:0; top:0;
  width:100%; height:100%;
  pointer-events:none;
  overflow:hidden;
}
.sparkle {
  position: absolute;
  width: 8px; height:8px;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.95), rgba(255,255,255,0.6) 30%, rgba(255,255,255,0) 60%);
  border-radius:50%;
  opacity:0.9;
  mix-blend-mode: screen;
  animation: drift 7s linear infinite;
}
@keyframes drift {
  0% { transform: translateY(-10vh) translateX(0) scale(0.7); opacity:0; }
  10% { opacity: 1; }
  60% { transform: translateY(60vh) translateX(6vw) scale(1.0); opacity: 0.9; }
  100% { transform: translateY(100vh) translateX(12vw) scale(0.6); opacity: 0; }
}

/* footer style */
.footer {
  text-align:center;
  color:#6b3b61;
  margin-top: 14px;
  font-size: 0.95rem;
}

/* small responsiveness */
@media (max-width:640px){
  .page-card { flex-direction: column; gap:12px; }
  .image-box { width: 200px; height: 150px; }
  .text-col { max-width: 100%; text-align:left; }
}
</style>
"""

# -------------------------
# Content
# -------------------------
IMG_DIR = Path("pages_for_nay_images")
# define pages (text taken from your earlier messages)
PAGES = [
    {
        "title": "How We Met",
        "quote": "Every story begins with a hello 💫",
        "text": "You were the first to say hello on HelloTalk. That same day we moved our chat to Instagram — and I discovered someone who loves books and cute things just like me. This is where our story began.",
        "img": IMG_DIR / "melody.png"
    },
    {
        "title": "The Cat Plushies",
        "quote": "A small plushie, a soft bond — and suddenly, we matched.",
        "text": "You sent me a picture of your cat plushie while we were chatting. A few days later I found a very similar one while shopping, and I couldn't resist buying it too. It felt like a silly little promise: two tiny plushies keeping our chats company.",
        "img": IMG_DIR / "plush.png"
    },
    {
        "title": "Girlhood Adventures",
        "quote": "If miles didn't matter, this would be us — soft days, sweet laughs, and a sky full of pink.",
        "text": "We daydream about pastel shops, sipping lattes in a cat cafe, painting by the ocean or in a park, and going on small food trips. Shopping, painting, and giggling together — all the little things that make a day feel like home.",
        "img": IMG_DIR / "panel.png"
    },
    {
        "title": "Dream Destinations",
        "quote": "Someday, Costa Rica to the Philippines — two dreamers finally meet.",
        "text": "I imagine visiting you in Costa Rica, learning about your culture and practicing Spanish while exploring beaches and markets. And then bringing you to the Philippines to discover pastel shops, street food, and long sunset walks. Real adventures from our chats.",
        "img": IMG_DIR / "plush.png"
    },
    {
        "title": "To Nay, on Your Birthday",
        "quote": "For the girl who feels like a calm melody — Happy Birthday, Nay 🎂💗",
        "text": dedent(\"\"\"Hi Nay!!!

Happy birthday — I hope your day begins with a big smile. It’s been months since we started talking, and I’m so grateful we still are. Meeting you felt like a fresh breeze: calm, kind, and bright. Thank you for coming into my life and for being such a warm and supportive friend.

I hope we get to meet in person someday, but for now I made you this little storybook. It’s a small, last-minute gift, but I kept my promise. Have so much fun today — I’ll be manifesting that TV and the giveaway for you (very hard). 🎁✨

Happy birthday again — love you lots!
— Katerenne\"\"\")
    }
]

# Session state
if "cover_opened" not in st.session_state:
    st.session_state.cover_opened = False
if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0
if "secret_unlocked" not in st.session_state:
    st.session_state.secret_unlocked = False

def open_book():
    st.session_state.cover_opened = True

def next_page():
    if st.session_state.page_idx < len(PAGES) - 1:
        st.session_state.page_idx += 1

def prev_page():
    if st.session_state.page_idx > 0:
        st.session_state.page_idx -= 1

def unlock_secret():
    st.session_state.secret_unlocked = True
    st.session_state.page_idx = len(PAGES)  # move to secret page

# Render UI
st.markdown(STYLE, unsafe_allow_html=True)
st.markdown('<div class="app-wrap">', unsafe_allow_html=True)

# audio player (visible)
audio_html = '<div style="display:flex;justify-content:center;margin-bottom:10px"><audio src="%s" controls loop preload="auto" style="width:90%%"></audio></div>' % AUDIO_SRC
st.markdown(audio_html, unsafe_allow_html=True)

# book frame
st.markdown('<div class="book-frame">', unsafe_allow_html=True)

# sparkles overlay
sparkles = (
    '<div class="sparkles">'
    '<div class="sparkle" style="left:8%; top:-2%; animation-duration:7s;"></div>'
    '<div class="sparkle" style="left:30%; top:-3%; animation-duration:6.5s; animation-delay:1.1s;"></div>'
    '<div class="sparkle" style="left:52%; top:-6%; animation-duration:8s; animation-delay:0.5s;"></div>'
    '<div class="sparkle" style="left:74%; top:-4%; animation-duration:7.2s; animation-delay:1.6s;"></div>'
    '</div>'
)
st.markdown(sparkles, unsafe_allow_html=True)

# COVER
if not st.session_state.cover_opened:
    st.markdown('<div class="title">Pages for Nay🩷</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A Birthday Story by Kate</div>', unsafe_allow_html=True)
    st.markdown('<div class="hint">Dedicated to my dear friend Nay — soft energy, calm smiles, and a bit of pink magic ✨</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)
    if st.button("💌 Open the Book"):
        open_book()

# SECRET PAGE
elif st.session_state.secret_unlocked:
    st.markdown('<div style="text-align:center; font-size:22px; color:#5b2b5d; font-weight:700">Secret Panel 🐾</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;color:#6b3b61;margin-bottom:12px">A tiny promise</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-card" style="flex-direction:column; align-items:center; text-align:center">', unsafe_allow_html=True)
    st.markdown('<div style="max-width:560px">One day, we’ll read this story together — not through a screen, but side by side. Maybe with a cat leaning on our laps, pastel drinks, and lots of easy laughter.<br><br><span style="color:#9b6ad6;font-weight:700">See you someday ♡</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Back to Start"):
        st.session_state.secret_unlocked = False
        st.session_state.page_idx = 0

# STORY PAGES
else:
    page = PAGES[st.session_state.page_idx]
    # quote
    st.markdown(f'<div style="text-align:center;font-style:italic;color:#6b3b61;margin-bottom:10px">{page["quote"]}</div>', unsafe_allow_html=True)

    # card with image + text (flip animation applied via .page-card)
    img_path = page.get("img")
    if img_path and Path(img_path).exists():
        left_html = f'<div><img src="{img_path.as_posix()}" style="width:220px;border-radius:10px;box-shadow:0 8px 18px rgba(120,60,120,0.08)"/></div>'
    else:
        left_html = '<div class="image-box">image missing</div>'

    right_html = f'<div class="text-col">{page["text"]}</div>'

    card_html = f'<div class="page-card">{left_html}{right_html}</div>'
    st.markdown(card_html, unsafe_allow_html=True)

    # centered nav (Prev / Secret Cat / Next)
    with st.container():
        c1, c2, c3 = st.columns([1, 0.9, 1])
        with c1:
            if st.button("◀ Previous"):
                prev_page()
        with c2:
            # center secret cat
            if st.button("🐱 Secret Cat"):
                unlock_secret()
        with c3:
            if st.button("Next ▶"):
                next_page()

# close book-frame and app-wrap
st.markdown('</div>', unsafe_allow_html=True)  # close book-frame
st.markdown('<div class="footer">Made with love by Kate💜</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # close app-wrap
