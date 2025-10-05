# app.py
# Pages for Nay - Streamlit Storybook (with generated chibi PNGs + flip animation)
# Run:
#   pip install streamlit pillow
#   streamlit run app.py

import streamlit as st
from textwrap import dedent
from pathlib import Path

st.set_page_config(page_title="Pages for Nay", page_icon="💌", layout="centered")

# Path to images directory (adjust if needed)
IMG_DIR = Path("pages_for_nay_images")  # put melody.png, kuromi.png, plush.png, panel.png here

# ---------- Replace this with your hosted mp3 if you have one ----------
AUDIO_SRC = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
# ---------------------------------------------------------------------------

# ---------- Styles (stronger colors + flip animation) ----------
STYLE = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&display=swap');

:root {{
  --bg1: #ff6fa3; /* pop pink */
  --bg2: #9b6ad6; /* vivid purple */
  --paper: rgba(255,255,255,0.98);
  --text: #3a2233;
}}

html, body, [class*="css"] {{
  background: linear-gradient(160deg, var(--bg1), var(--bg2));
  color: var(--text);
  font-family: Poppins, "Segoe UI", sans-serif;
  min-height:100vh;
}}

/* app container */
.app-container {{
  max-width: 760px;
  margin: 18px auto;
  padding: 16px;
  text-align: center;
}}

/* Book / scrapbook frame */
.book-frame {{
  background: linear-gradient(180deg, rgba(255,255,255,0.98), var(--paper));
  border-radius: 18px;
  box-shadow: 0 18px 40px rgba(59, 31, 69, 0.18), inset 0 1px 0 rgba(255,255,255,0.6);
  padding: 24px;
  margin: 12px auto;
  max-width: 700px;
  min-height: 460px;
  position: relative;
  overflow: hidden;
}}

/* flip animation for page body */
.page-body {{
  transform-origin: center;
  animation: flipIn 0.6s ease;
}}
@keyframes flipIn {{
  0% {{ transform: rotateY(-90deg) translateY(10px); opacity: 0; }}
  60% {{ transform: rotateY(10deg) translateY(0); opacity: 0.9; }}
  100% {{ transform: rotateY(0deg) translateY(0); opacity: 1; }}
}}

/* title and cursive */
.cover-title {{
  font-family: "Great Vibes", cursive;
  font-size: 2.6rem;
  color: #5a2350;
  margin-bottom: 4px;
  letter-spacing: 0.6px;
}}
.cover-sub {{
  color: rgba(90,40,70,0.9);
  margin-bottom: 14px;
  font-size: 1rem;
}}

/* page content */
.page-title {{
  font-size: 1.4rem;
  color: #5d2d61;
  font-weight: 700;
}}
.page-sub {{
  color: #7d4d77;
  margin-bottom: 12px;
}}
.page-body {{
  text-align: left;
  color: #3f2b3a;
  line-height: 1.6;
  font-size: 1rem;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.99));
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(110,60,100,0.04);
}

/* centered nav */
.nav-row {{
  display:flex;
  gap:12px;
  justify-content:center;
  align-items:center;
  margin-top:14px;
}}

/* buttons */
.btn {{
  background: linear-gradient(90deg,#9b6ad6,#ff8fb3);
  color: white;
  padding: 10px 18px;
  border-radius: 14px;
  font-weight: 600;
  border: none;
  box-shadow: 0 8px 20px rgba(170,90,150,0.12);
  cursor: pointer;
}}

/* secret cat centered */
.secret-wrapper {{
  display:flex;
  justify-content:center;
  align-items:center;
  margin-top: 8px;
}}

/* sparkles */
.sparkles {{
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
}}
.sparkle {{
  position: absolute;
  width: 8px;
  height: 8px;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.95), rgba(255,255,255,0.6) 30%, rgba(255,255,255,0.0) 60%);
  border-radius: 50%;
  opacity: 0.9;
  transform: translateY(-10vh) scale(0.7);
  animation: drift 6s linear infinite;
  mix-blend-mode: screen;
}}
@keyframes drift {{
  0% {{ transform: translateY(-6vh) translateX(0) scale(0.6); opacity: 0.0; }}
  10% {{ opacity: 1; }}
  50% {{ transform: translateY(60vh) translateX(12vw) scale(1.0); opacity: 0.9; }}
  95% {{ opacity: 0.4; }}
  100% {{ transform: translateY(90vh) translateX(18vw) scale(0.7); opacity: 0; }}
}}

@media (max-width:640px) {{
  .cover-title {{ font-size: 2.2rem; }}
  .book-frame {{ padding: 16px; min-height: 520px; }}
  .page-body {{ font-size: 0.98rem; }}
}}
</style>
"""

# ---------- Story content (same as before) ----------
PAGES = [
    {
        "title": "How We Met",
        "quote": "Every story begins with a hello 💫",
        "text": (
            "You were the first to say hello on HelloTalk. That same day we moved our chat to Instagram — "
            "and I discovered someone who loves books and cute things just like me. "
            "This is where our story began."
        ),
        "img": IMG_DIR / "melody.png"
    },
    {
        "title": "The Cat Plushies",
        "quote": "A small plushie, a soft bond — and suddenly, we matched.",
        "text": (
            "You sent me a picture of your cat plushie while we were chatting. A few days later I found a very similar one while shopping, "
            "and I couldn't resist buying it too. It felt like a silly little promise: two tiny plushies keeping our chats company."
        ),
        "img": IMG_DIR / "plush.png"
    },
    {
        "title": "Girlhood Adventures",
        "quote": "If miles didn't matter, this would be us — soft days, sweet laughs, and a sky full of pink.",
        "text": (
            "We daydream about pastel shops, sipping lattes in a cat cafe, painting by the ocean or in a park, and going on small food trips. "
            "Shopping, painting, and giggling together — all the little things that make a day feel like home."
        ),
        "img": IMG_DIR / "panel.png"
    },
    {
        "title": "Dream Destinations",
        "quote": "Someday, Costa Rica to the Philippines — two dreamers finally meet.",
        "text": (
            "I imagine visiting you in Costa Rica, learning about your culture and practicing Spanish while exploring beaches and markets. "
            "And then bringing you to the Philippines to discover pastel shops, street food, and long sunset walks. Real adventures from our chats."
        ),
        "img": IMG_DIR / "plush.png"
    },
    {
        "title": "To Nay, on Your Birthday",
        "quote": "For the girl who feels like a calm melody — Happy Birthday, Nay 🎂💗",
        "text": dedent("""
        Hi Nay!!!

        Happy birthday — I hope your day begins with a big smile. It’s been months since we started talking, and I’m so grateful we still are. Meeting you felt like a fresh breeze: calm, kind, and bright. Thank you for coming into my life and for being such a warm and supportive friend.

        I hope we get to meet in person someday, but for now I made you this little storybook. It’s a small, last-minute gift, but I kept my promise. Have so much fun today — I’ll be manifesting that TV and the giveaway for you (very hard). 🎁✨

        Happy birthday again — love you lots!
        — Katerenne
        """).strip(),
        "img": IMG_DIR / "melody.png"
    }
]

# ---------- Session state ----------
if "cover_opened" not in st.session_state:
    st.session_state.cover_opened = False
if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0
if "secret" not in st.session_state:
    st.session_state.secret = False

def open_book():
    st.session_state.cover_opened = True

def next_page():
    if st.session_state.page_idx < len(PAGES) - 1:
        st.session_state.page_idx += 1

def prev_page():
    if st.session_state.page_idx > 0:
        st.session_state.page_idx -= 1

def unlock_secret():
    st.session_state.secret = True
    st.session_state.page_idx = len(PAGES)

def back_to_book():
    st.session_state.secret = False
    st.session_state.page_idx = 0

# ---------- Render ----------
st.markdown(STYLE, unsafe_allow_html=True)
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# audio (player visible)
audio_html = f"""
<div style="display:flex;justify-content:center;margin-bottom:6px">
  <audio src="{AUDIO_SRC}" controls loop preload="auto" style="outline:none;width:90%"></audio>
</div>
"""
st.markdown(audio_html, unsafe_allow_html=True)

st.markdown('<div class="book-frame">', unsafe_allow_html=True)

# sparkles
sparkles_html = """
<div class="sparkles">
  <div class="sparkle" style="left:6%; top:-4%; animation-duration:7s; animation-delay:0s;"></div>
  <div class="sparkle" style="left:26%; top:-2%; animation-duration:6.5s; animation-delay:1.2s;"></div>
  <div class="sparkle" style="left:46%; top:-6%; animation-duration:8s; animation-delay:0.5s;"></div>
  <div class="sparkle" style="left:66%; top:-4%; animation-duration:7.2s; animation-delay:1.6s;"></div>
  <div class="sparkle" style="left:86%; top:-3%; animation-duration:6.8s; animation-delay:0.2s;"></div>
</div>
"""
st.markdown(sparkles_html, unsafe_allow_html=True)

# COVER
if not st.session_state.cover_opened:
    st.markdown('<div class="cover-title">🎀 Pages for Nay</div>', unsafe_allow_html=True)
    st.markdown('<div class="cover-sub">A Birthday Story by Katerenne</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#6a3a5f;margin-bottom:18px">Dedicated to my dear friend Nay — soft energy, calm smiles, and a bit of pink magic ✨</div>', unsafe_allow_html=True)
    if st.button("💌 Open the Book", key="open"):
        open_book()

# STORY PAGES
elif not st.session_state.secret and st.session_state.page_idx < len(PAGES):
    page = PAGES[st.session_state.page_idx]

    st.markdown(f'<div style="font-style:italic;color:#6b3b61;margin-bottom:8px">{page["quote"]}</div>', unsafe_allow_html=True)

    # show image + text with flip animation class
    cols = st.columns([1,1.2])
    with cols[0]:
        if page["img"].exists():
            st.image(str(page["img"]), use_column_width=True)
        else:
            st.info("Image not found. Put images in pages_for_nay_images/ folder.")
    with cols[1]:
        st.markdown(f'<div class="page-body">{page["text"]}</div>', unsafe_allow_html=True)

    # centered navigation + secret cat
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        if st.button("◀ Prev"):
            prev_page()
    with c2:
        if st.button("🐱 Secret Cat"):
            unlock_secret()
    with c3:
        if st.button("Next ▶"):
            next_page()
    st.markdown('</div>', unsafe_allow_html=True)

# SECRET PAGE
else:
    secret_html = """
    <div style="padding:12px">
      <div style="font-size:1.25rem;color:#5d2d61;font-weight:700;margin-bottom:6px">Secret Panel 🐾</div>
      <div style="color:#6b3b61;margin-bottom:10px">A tiny promise</div>
      <div class="page-body" style="text-align:center">
        <p>One day, we’ll read this story together — not through a screen, but side by side. Maybe with a cat leaning on our laps, pastel drinks, and lots of easy laughter.</p>
        <p style="color:#b58ed6;font-weight:700;margin-top:8px">See you someday ♡</p>
      </div>
      <div style="margin-top:12px">
        <button class="btn" onclick="window.location.href = window.location.pathname">Back to Book</button>
      </div>
    </div>
    """
    st.markdown(secret_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;margin-top:12px;color:#6b3b61;font-size:0.95rem">Made with care — a soft story for Nay 💗</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
