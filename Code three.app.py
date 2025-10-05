# app.py
# Pages for Nay - Streamlit Storybook (Updated version with front cover, stronger colors, centered nav)

import streamlit as st
from textwrap import dedent

st.set_page_config(page_title="Pages for Nay 💌", page_icon="🎀", layout="centered")

# -------------------------
# Styling (deep pink + purple)
# -------------------------
STYLE = """
<style>
:root {
  --pink: #f4a3c2;
  --purple: #b58ed6;
  --cream: #fff7fb;
  --text: #3b2b3b;
}
html, body, [class*="css"]  {
  background: linear-gradient(180deg, var(--pink), #fff);
  color: var(--text);
  font-family: "Poppins", "Comic Neue", "Segoe UI", sans-serif;
}
.container {
  background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(255,255,255,0.92));
  padding: 28px;
  border-radius: 18px;
  box-shadow: 0 12px 30px rgba(170,100,180,0.15);
  text-align: center;
  max-width: 680px;
  margin: auto;
}
.cover-title {
  font-size: 2.4rem;
  color: var(--purple);
  margin-bottom: 8px;
  font-weight: 700;
}
.cover-sub {
  color: #6a4466;
  margin-bottom: 18px;
}
.navbar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 14px;
  margin-top: 12px;
}
.nav-btn {
  background: linear-gradient(90deg,var(--purple), var(--pink));
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 14px;
  font-weight: 600;
  cursor: pointer;
}
.small {
  color:#8f748e;
  font-size: 0.9rem;
}
.page-wrap {
  min-height: 360px;
  display: flex;
  gap: 16px;
  align-items: center;
  justify-content: center;
  padding: 18px;
}
.panel {
  background: white;
  border-radius: 14px;
  padding: 18px;
  width: 560px;
  max-width: 90%;
  box-shadow: 0 10px 28px rgba(180,140,180,0.12);
  animation: fadeIn 0.45s ease;
}
.title {
  color: var(--purple);
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.subtitle {
  color: #9b718f;
  margin-bottom: 12px;
}
.content {
  color: #422d42;
  line-height: 1.6;
  font-size: 1rem;
}
.cat-secret {
  font-size: 28px;
  cursor: pointer;
  opacity: 0.95;
  transition: transform 0.18s ease;
}
.cat-secret:hover { transform: scale(1.08); }
.footer {
  margin-top: 14px;
  color:#7b5b73;
  font-size:0.9rem;
}
@keyframes fadeIn {
  from { transform: translateY(6px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
</style>
"""

# -------------------------
# SVG chibis
# -------------------------
def svg_melody():
    return dedent("""
    <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
      <rect rx="14" width="120" height="120" fill="#ffd6e8"/>
      <ellipse cx="60" cy="68" rx="34" ry="28" fill="#ffe0eb"/>
      <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
      <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
      <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Melody</text>
    </svg>
    """)

def svg_kuromi():
    return dedent("""
    <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
      <rect rx="14" width="120" height="120" fill="#e6d6ff"/>
      <ellipse cx="60" cy="68" rx="34" ry="28" fill="#f1e4ff"/>
      <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
      <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
      <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Kuromi</text>
    </svg>
    """)

# -------------------------
# Story pages
# -------------------------
PAGES = [
    {
        "title": "How We Met",
        "subtitle": "HelloTalk → Instagram",
        "text": (
            "You were the first to say hello on HelloTalk. That same day we moved our chat to Instagram — "
            "and I found someone who loves books and cute things just like me. "
            "This is where our story began."
        ),
        "svg": svg_melody()
    },
    {
        "title": "The Cat Plushies",
        "subtitle": "A tiny matching tradition",
        "text": (
            "You sent me a picture of your cat plushie, and later, while shopping, I found one that looked so similar. "
            "I bought it too — a small, silly thing, but it felt like a tiny promise between us."
        ),
        "svg": svg_kuromi()
    },
    {
        "title": "Girlhood Adventures",
        "subtitle": "Shopping, cafes, painting, treats",
        "text": (
            "We daydream about simple, perfect days together: wandering pastel shops, sipping sweet lattes in a cat cafe, "
            "painting by the ocean or in the park, and baking or going on little food trips. "
            "So many small, soft moments to look forward to."
        ),
        "svg": svg_melody()
    },
    {
        "title": "Dream Destinations",
        "subtitle": "Philippines ↔ Costa Rica",
        "text": (
            "One day I visit you in Costa Rica — learning about your culture and practicing Spanish while exploring little "
            "streets and beaches. Another day you come to the Philippines and we lose ourselves in pastel shops, street food, "
            "and sunsets by the bay. Adventures that start as chats, someday real."
        ),
        "svg": svg_kuromi()
    },
    {
        "title": "To Nay, on Your Birthday",
        "subtitle": "My little letter",
        "text": dedent("""
        Hi Nay!!!

        Happy birthday — I hope your day begins with a big smile. It’s been months since we started talking, and I’m so grateful we still are. Meeting you felt like a fresh breeze: calm, kind, and bright. Thank you for coming into my life and for being such a warm and supportive friend.

        I hope we get to meet in person someday, but for now I made you this little storybook. It’s a small, last-minute gift, but I kept my promise. Have so much fun today — I’ll be manifesting that TV and the giveaway for you (very hard). 🎁✨

        Happy birthday again — love you lots!
        — Katerenne
        """).strip(),
        "svg": svg_melody()
    }
]

# -------------------------
# Session state
# -------------------------
if "cover_opened" not in st.session_state:
    st.session_state.cover_opened = False
if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0
if "secret_unlocked" not in st.session_state:
    st.session_state.secret_unlocked = False

def go_next():
    if st.session_state.page_idx < len(PAGES)-1:
        st.session_state.page_idx += 1

def go_prev():
    if st.session_state.page_idx > 0:
        st.session_state.page_idx -= 1

def unlock_secret():
    st.session_state.secret_unlocked = True
    st.session_state.page_idx = len(PAGES)

# -------------------------
# Render
# -------------------------
st.markdown(STYLE, unsafe_allow_html=True)
st.markdown('<div class="container">', unsafe_allow_html=True)

# FRONT COVER
if not st.session_state.cover_opened:
    st.markdown("""
    <div class="cover-title">🎀 Pages for Nay 🎀</div>
    <div class="cover-sub">A Birthday Story by Katerenne</div>
    <div style="font-size:0.95rem;color:#6f4c66;margin-bottom:20px">
    Dedicated to my dear friend Nay, who brings soft energy, calm smiles, and a bit of pink magic into my world.
    </div>
    """, unsafe_allow_html=True)
    if st.button("💌 Open the Book"):
        st.session_state.cover_opened = True

# STORYBOOK
elif not st.session_state.secret_unlocked and st.session_state.page_idx < len(PAGES):
    page = PAGES[st.session_state.page_idx]
    html_panel = f"""
    <div class="page-wrap">
      <div class="panel">
        <div class="title">{page['title']}</div>
        <div class="subtitle">{page['subtitle']}</div>
        <div class="content" style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;justify-content:center">
          <div>{page['svg']}</div>
          <div style="max-width:360px;text-align:left;white-space:pre-line">{page['text']}</div>
        </div>
      </div>
    </div>
    """
    st.components.v1.html(html_panel, height=420)

    # Navigation buttons (centered)
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("◀ Prev"):
            go_prev()
    with col2:
        if st.button("🐱 Secret Cat"):
            unlock_secret()
    with col3:
        if st.button("Next ▶"):
            go_next()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    secret_html = """
    <div class="page-wrap">
      <div class="panel">
        <div class="title">Secret Page 🐾</div>
        <div class="subtitle">A tiny promise</div>
        <div class="content">
          <p>One day, we’ll read this story not through a screen, but side by side — maybe with a cat near us, pastel drinks, and easy laughter.</p>
          <p style="color:#b58ed6;font-weight:700">See you someday ♡</p>
        </div>
      </div>
    </div>
    """
    st.components.v1.html(secret_html, height=380)
    if st.button("Back to Book"):
        st.session_state.secret_unlocked = False
        st.session_state.page_idx = 0

st.markdown('</div>', unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center;margin-top:12px;color:#7b5b73;font-size:0.9rem'>Made with care — a soft story for Nay 💗</div>",
    unsafe_allow_html=True
)
