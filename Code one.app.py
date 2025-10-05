# app.py
# Pages for Nay - Streamlit Storybook
# Requires: streamlit
# Run: pip install streamlit
#      streamlit run app.py

import streamlit as st
from textwrap import dedent

st.set_page_config(page_title="Pages for Nay", page_icon="💌", layout="centered")

# -------------------------
# Styling (pink + purple)
# -------------------------
STYLE = """
<style>
:root{
  --pink: #f9c6d0;
  --purple: #c9a6e0;
  --cream: #fff7fb;
  --text: #3b2b3b;
}
html, body, [class*="css"]  {
  background: linear-gradient(180deg, var(--pink), #fff);
  color: var(--text);
  font-family: "Poppins", "Comic Neue", "Segoe UI", sans-serif;
}
.container {
  background: linear-gradient(180deg, rgba(255,255,255,0.75), rgba(255,255,255,0.9));
  padding: 22px;
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(160,120,180,0.08);
}
.cover-title {
  font-size: 2.2rem;
  color: var(--purple);
  margin-bottom: 6px;
  font-weight: 700;
}
.cover-sub {
  color: #8b6b86;
  margin-bottom: 12px;
}
.nav-btn {
  background: linear-gradient(90deg,var(--purple), #b58ed6);
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 12px;
  font-weight: 600;
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
  border-radius: 12px;
  padding: 14px;
  width: 560px;
  max-width: 90%;
  box-shadow: 0 10px 30px rgba(180,140,180,0.06);
  animation: fadeIn 0.45s ease;
}
.title {
  color: var(--purple);
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.subtitle {
  color: #9b718f;
  margin-bottom: 12px;
}
.content {
  color: #422d42;
  line-height: 1.5;
}
.comic-row {
  display:flex;
  gap:12px;
  margin-top:12px;
  flex-wrap:wrap;
  justify-content:center;
}
.panel-comic {
  background: linear-gradient(180deg,#fff,#fff8ff);
  padding:10px;
  border-radius:10px;
  border:1px dashed rgba(180,140,180,0.22);
  text-align:center;
  width: 160px;
}
.caption { font-size:0.9rem; color:#7a556e; margin-top:6px; }
.cat-secret {
  font-size:28px;
  cursor:pointer;
  opacity:0.95;
  transition: transform 0.18s ease;
}
.cat-secret:hover { transform: scale(1.06); }
.footer {
  margin-top: 12px;
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
# Simple SVG chibi panels
# -------------------------
# We create minimal SVG illustrations for Melody (pink/white ears) and Kuromi (purple-ish).
def svg_melody():
    return dedent("""
    <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
      <rect rx="14" width="120" height="120" fill="#fff0f6"/>
      <ellipse cx="60" cy="68" rx="34" ry="28" fill="#ffeaf2"/>
      <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
      <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
      <!-- bow -->
      <ellipse cx="32" cy="32" rx="14" ry="10" fill="#ffd2e6"/>
      <ellipse cx="46" cy="32" rx="10" ry="8" fill="#ffc2dc"/>
      <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Melody</text>
    </svg>
    """)

def svg_kuromi():
    return dedent("""
    <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
      <rect rx="14" width="120" height="120" fill="#f6f0ff"/>
      <ellipse cx="60" cy="68" rx="34" ry="28" fill="#f3e6ff"/>
      <circle cx="45" cy="50" r="6" fill="#2b2b2b"/>
      <circle cx="75" cy="50" r="6" fill="#2b2b2b"/>
      <!-- little horn/hat accent -->
      <path d="M36 28 Q48 10 60 28" fill="#d6b4ff"/>
      <text x="60" y="105" font-size="10" text-anchor="middle" fill="#7a556e">Kuromi</text>
    </svg>
    """)

def svg_plushies():
    return dedent("""
    <svg width="280" height="120" viewBox="0 0 280 120" xmlns="http://www.w3.org/2000/svg">
      <rect rx="8" width="280" height="120" fill="#fff"/>
      <!-- left plush -->
      <circle cx="70" cy="60" r="36" fill="#ffdfe9"/>
      <circle cx="56" cy="52" r="6" fill="#2b2b2b"/>
      <circle cx="84" cy="52" r="6" fill="#2b2b2b"/>
      <!-- right plush -->
      <circle cx="210" cy="60" r="36" fill="#f3e6ff"/>
      <circle cx="196" cy="52" r="6" fill="#2b2b2b"/>
      <circle cx="224" cy="52" r="6" fill="#2b2b2b"/>
      <text x="140" y="105" text-anchor="middle" font-size="11" fill="#7b556e">Matching plushies</text>
    </svg>
    """)

# -------------------------
# Story content (you provided; slightly cleaned)
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
        "svg": svg_plushies()
    },
    {
        "title": "Girlhood Adventures",
        "subtitle": "Shopping, cafes, painting, treats",
        "text": (
            "We daydream about simple, perfect days together: wandering pastel shops, sipping sweet lattes in a cat cafe, "
            "painting by the ocean or in the park, and baking or going on little food trips. "
            "So many small, soft moments to look forward to."
        ),
        "svg": svg_kuromi()
    },
    {
        "title": "Dream Destinations",
        "subtitle": "Philippines ↔ Costa Rica",
        "text": (
            "One day I visit you in Costa Rica — learning about your culture and practicing Spanish while exploring little "
            "streets and beaches. Another day you come to the Philippines and we lose ourselves in pastel shops, street food, "
            "and sunsets by the bay. Adventures that start as chats, someday real."
        ),
        "svg": svg_plushies()
    },
    {
        "title": "To Nay, on Your Birthday",
        "subtitle": "My little letter",
        "text": None,  # we'll use the full polished letter below
        "svg": svg_melody()
    }
]

# final polished birthday text inserted on last page
FINAL_MESSAGE = dedent("""
Hi Nay!!!

Happy birthday — I hope your day begins with a big smile. It’s been months since we started talking, and I’m so grateful we still are. Meeting you felt like a fresh breeze: calm, kind, and bright. Thank you for coming into my life and for being such a warm and supportive friend.

I hope we get to meet in person someday, but for now I made you this little storybook. It’s a small, last-minute gift, but I kept my promise. Have so much fun today — I’ll be manifesting that TV and the giveaway for you (very hard). 🎁✨

Happy birthday again — love you lots!
— Katerenne
""").strip()

# -------------------------
# Session state & navigation
# -------------------------
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
    st.session_state.page_idx = len(PAGES)  # go to secret after pages

# -------------------------
# Page layout
# -------------------------
st.markdown(STYLE, unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

# cover-like header on top
st.markdown(f'<div style="text-align:center"><div class="cover-title">Pages for Nay 💌</div>'
            f'<div class="cover-sub">A little story for your birthday</div></div>', unsafe_allow_html=True)

# render either main pages or secret page
if st.session_state.page_idx < len(PAGES):
    page = PAGES[st.session_state.page_idx]

    # show panel
    html_panel = f"""
    <div class="page-wrap">
      <div class="panel">
        <div class="title">{page['title']}</div>
        <div class="subtitle">{page['subtitle']}</div>
        <div class="content">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:center">
            <div style="min-width:140px">{page['svg']}</div>
            <div style="max-width:360px;text-align:left">{page['text'] if page['text'] else FINAL_MESSAGE}</div>
          </div>
          <div class="comic-row">
            <!-- small comic panels -->
            <div class="panel-comic">{svg_melody()}<div class="caption">Melody</div></div>
            <div class="panel-comic">{svg_kuromi()}<div class="caption">Kuromi</div></div>
          </div>
        </div>
      </div>
    </div>
    """
    st.components.v1.html(html_panel, height=420)

    # navigation row
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("◀ Prev"):
            go_prev()
    with col2:
        # hidden cat (center) to unlock secret
        st.markdown('<div style="text-align:center;margin-top:8px">'
                    '<span class="small">click the cat to unlock a secret</span><br>'
                    '<span class="cat-secret" title="Secret" onclick="document.querySelectorAll(\\'.stButton\\')[0].click()">🐱</span>'
                    '</div>',
                    unsafe_allow_html=True)
        # NOTE: the small hack above triggers the first button via onclick only in browser JS.
        # To reliably unlock in Streamlit, also provide an ordinary button below:
        if st.button("🐱 Secret Cat"):
            unlock_secret()
    with col3:
        if st.button("Next ▶"):
            go_next()

    st.markdown('<div class="footer">Tip: Click the cat or the "Secret Cat" button for a surprise.</div>', unsafe_allow_html=True)

else:
    # secret page content
    secret_html = """
    <div class="page-wrap">
      <div class="panel">
        <div class="title">Secret Panel</div>
        <div class="subtitle">A tiny promise</div>
        <div class="content">
          <p>One day, we will read this story together — not through screens, but side by side.</p>
          <p class="heart" style="color:#c9a6e0;font-weight:700">See you someday ♡</p>
          <div style="margin-top:12px;text-align:center">
            <svg width="260" height="120" viewBox="0 0 260 120" xmlns="http://www.w3.org/2000/svg">
              <rect rx="12" width="260" height="120" fill="#fff"/>
              <circle cx="70" cy="60" r="32" fill="#ffdfe9"/>
              <circle cx="190" cy="60" r="32" fill="#f3e6ff"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
    """
    st.components.v1.html(secret_html, height=380)
    if st.button("Back to Book"):
        st.session_state.secret_unlocked = False
        st.session_state.page_idx = 0

st.markdown('</div>', unsafe_allow_html=True)

# Optional: small footer
st.markdown("<div style='text-align:center;margin-top:10px;color:#87606f;font-size:0.9rem'>Made with care — a soft story for Nay 💗</div>", unsafe_allow_html=True)
