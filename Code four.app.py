# app.py
# Pages for Nay - Streamlit Storybook (Scrapbook feel, sparkles, cursive font, music)
# Run:
#   pip install streamlit
#   streamlit run app.py

import streamlit as st
from textwrap import dedent

st.set_page_config(page_title="Pages for Nay", page_icon="💌", layout="centered")

# ---------- Replace this with your own hosted mp3 if you have one ----------
AUDIO_SRC = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
# ---------------------------------------------------------------------------

# ---------- Styles ----------
STYLE = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&display=swap');

:root {{
  --bg1: #ff8fb3; /* vivid pink */
  --bg2: #b58ed6; /* purple */
  --paper: rgba(255,255,255,0.98);
  --accent: #ffb3d0;
  --text: #372336;
}}

html, body, [class*="css"] {{
  background: linear-gradient(160deg, var(--bg1), var(--bg2));
  color: var(--text);
  font-family: Poppins, "Segoe UI", sans-serif;
  height:100%;
}}

/* app container */
.app-container {{
  max-width: 760px;
  margin: 22px auto;
  padding: 20px;
  text-align: center;
}}

/* Book / scrapbook frame */
.book-frame {{
  background: linear-gradient(180deg, rgba(255,255,255,0.96), var(--paper));
  border-radius: 18px;
  box-shadow: 0 18px 40px rgba(59, 31, 69, 0.18), inset 0 1px 0 rgba(255,255,255,0.6);
  padding: 28px;
  margin: 12px auto;
  max-width: 680px;
  min-height: 420px;
  position: relative;
  overflow: hidden;
}}

/* faux paper edges (scrapbook look) */
.book-frame:before {{
  content: "";
  position: absolute;
  left: 12px;
  right: 12px;
  top: 6px;
  bottom: 6px;
  border-radius: 14px;
  box-shadow: 0 6px 18px rgba(120,70,130,0.05) inset;
  pointer-events: none;
}}

/* title and cursive */
.cover-title {{
  font-family: "Great Vibes", cursive;
  font-size: 3rem;
  color: #6a2a57;
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
  padding: 14px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(110,60,100,0.04);
}}

/* comic row (small icons) */
.comic-row {{
  display:flex;
  gap:12px;
  margin-top:12px;
  justify-content:center;
  flex-wrap:wrap;
}}

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
  background: linear-gradient(90deg,#b58ed6,#ff9fc6);
  color: white;
  padding: 10px 18px;
  border-radius: 14px;
  font-weight: 600;
  border: none;
  box-shadow: 0 8px 20px rgba(170,90,150,0.12);
  cursor: pointer;
}}

/* small hint */
.hint {{
  color: rgba(80,44,76,0.9);
  font-size: 0.9rem;
}}

/* secret cat centered */
.secret-wrapper {{
  display:flex;
  justify-content:center;
  align-items:center;
  margin-top: 8px;
}}

/* sparkles animation - subtle */
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
}
@keyframes drift {{
  0% {{ transform: translateY(-6vh) translateX(0) scale(0.6); opacity: 0.0; }}
  10% {{ opacity: 1; }}
  50% {{ transform: translateY(60vh) translateX(12vw) scale(1.0); opacity: 0.9; }}
  95% {{ opacity: 0.4; }}
  100% {{ transform: translateY(90vh) translateX(18vw) scale(0.7); opacity: 0; }}
}}

/* small responsive tweaks */
@media (max-width:640px) {{
  .cover-title {{ font-size: 2.2rem; }}
  .book-frame {{ padding: 18px; min-height: 480px; }}
  .page-body {{ font-size: 0.98rem; }}
}}
</style>
"""

# ---------- Inline small SVGs for chibi & plushie ----------
SVG_MELODY = dedent("""
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <rect rx="14" width="120" height="120" fill="#ffd6e8"/>
  <ellipse cx="60" cy="68" rx="34" ry="28" fill="#ffe0eb"/>
  <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
  <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
  <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Melody</text>
</svg>
""")

SVG_KUROMI = dedent("""
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <rect rx="14" width="120" height="120" fill="#e6d6ff"/>
  <ellipse cx="60" cy="68" rx="34" ry="28" fill="#f1e4ff"/>
  <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
  <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
  <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Kuromi</text>
</svg>
""")

SVG_PLUSH = dedent("""
<svg width="260" height="120" viewBox="0 0 260 120" xmlns="http://www.w3.org/2000/svg">
  <rect rx="10" width="260" height="120" fill="#fff"/>
  <circle cx="70" cy="60" r="36" fill="#ffdfe9"/>
  <circle cx="56" cy="52" r="6" fill="#2b2b2b"/>
  <circle cx="84" cy="52" r="6" fill="#2b2b2b"/>
  <circle cx="190" cy="60" r="36" fill="#f3e6ff"/>
  <circle cx="176" cy="52" r="6" fill="#2b2b2b"/>
  <circle cx="204" cy="52" r="6" fill="#2b2b2b"/>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#7b556e">Matching plushies</text>
</svg>
""")

# ---------- Story content + transitions ----------
PAGES = [
    {
        "title": "How We Met",
        "quote": "Every story begins with a hello 💫",
        "text": (
            "You were the first to say hello on HelloTalk. That same day we moved our chat to Instagram — "
            "and I discovered someone who loves books and cute things just like me. "
            "This is where our story began."
        ),
        "svg": SVG_MELODY
    },
    {
        "title": "The Cat Plushies",
        "quote": "A small plushie, a soft bond — and suddenly, we matched.",
        "text": (
            "You sent me a picture of your cat plushie while we were chatting. A few days later I found a very similar one while shopping, "
            "and I couldn't resist buying it too. It felt like a silly little promise: two tiny plushies keeping our chats company."
        ),
        "svg": SVG_PLUSH
    },
    {
        "title": "Girlhood Adventures",
        "quote": "If miles didn't matter, this would be us — soft days, sweet laughs, and a sky full of pink.",
        "text": (
            "We daydream about pastel shops, sipping lattes in a cat cafe, painting by the ocean or in a park, and going on small food trips. "
            "Shopping, painting, and giggling together — all the little things that make a day feel like home."
        ),
        "svg": SVG_KUROMI
    },
    {
        "title": "Dream Destinations",
        "quote": "Someday, Costa Rica to the Philippines — two dreamers finally meet.",
        "text": (
            "I imagine visiting you in Costa Rica, learning about your culture and practicing Spanish while exploring beaches and markets. "
            "And then bringing you to the Philippines to discover pastel shops, street food, and long sunset walks. Real adventures from our chats."
        ),
        "svg": SVG_PLUSH
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
        "svg": SVG_MELODY
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

# Embed audio with autoplay + controls (browsers may block autoplay until user interacts)
audio_html = f"""
<div style="display:flex;justify-content:center;margin-bottom:6px">
  <audio src="{AUDIO_SRC}" controls loop preload="auto" style="outline:none"></audio>
</div>
"""
st.markdown(audio_html, unsafe_allow_html=True)

# Book frame container
st.markdown('<div class="book-frame">', unsafe_allow_html=True)

# sparkles: create a few sparkles at different positions and delays
sparkles_html = """
<div class="sparkles">
  <div class="sparkle" style="left:8%; top:-4%; animation-duration:7s; animation-delay:0s; width:8px; height:8px;"></div>
  <div class="sparkle" style="left:22%; top:-2%; animation-duration:6.5s; animation-delay:1.2s; width:10px; height:10px;"></div>
  <div class="sparkle" style="left:44%; top:-6%; animation-duration:8s; animation-delay:0.5s; width:6px; height:6px;"></div>
  <div class="sparkle" style="left:66%; top:-4%; animation-duration:7.2s; animation-delay:1.6s; width:9px; height:9px;"></div>
  <div class="sparkle" style="left:86%; top:-3%; animation-duration:6.8s; animation-delay:0.2s; width:7px; height:7px;"></div>
</div>
"""
st.markdown(sparkles_html, unsafe_allow_html=True)

# COVER
if not st.session_state.cover_opened:
    st.markdown('<div class="cover-title">🎀 Pages for Nay</div>', unsafe_allow_html=True)
    st.markdown('<div class="cover-sub">A Birthday Story by Katerenne</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#6a3a5f;margin-bottom:18px">Dedicated to my dear friend Nay — soft energy, calm smiles, and a bit of pink magic ✨</div>', unsafe_allow_html=True)
    if st.button("💌 Open the Book", key="open", help="Open the storybook"):
        open_book()

# STORY PAGES
elif not st.session_state.secret and st.session_state.page_idx < len(PAGES):
    page = PAGES[st.session_state.page_idx]

    # Quote line
    st.markdown(f'<div style="font-style:italic;color:#6b3b61;margin-bottom:8px">{page["quote"]}</div>', unsafe_allow_html=True)

    # page content inside faux paper block
    page_html = f"""
    <div class="page-body" role="article">
      <div style="display:flex;gap:18px;align-items:center;justify-content:center;flex-wrap:wrap">
        <div style="min-width:140px">{page['svg']}</div>
        <div style="max-width:420px;text-align:left;white-space:pre-line">{page['text']}</div>
      </div>
    </div>
    """
    st.markdown(page_html, unsafe_allow_html=True)

    # small comic row (two chibis)
    st.markdown('<div class="comic-row">', unsafe_allow_html=True)
    st.markdown(f'<div style="width:140px">{SVG_MELODY}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="width:140px">{SVG_KUROMI}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # centered navigation + secret cat
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    cols = st.columns([1, 1, 1])
    with cols[0]:
        if st.button("◀ Prev"):
            prev_page()
    with cols[1]:
        # secret cat button centered here
        st.markdown('<div class="secret-wrapper">', unsafe_allow_html=True)
        if st.button("🐱 Secret Cat"):
            unlock_secret()
        st.markdown('</div>', unsafe_allow_html=True)
    with cols[2]:
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

st.markdown('</div>', unsafe_allow_html=True)  # close book-frame
st.markdown('<div style="text-align:center;margin-top:10px;color:#6b3b61;font-size:0.95rem">Made with care — a soft story for Nay 💗</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # close app-container
