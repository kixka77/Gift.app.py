import streamlit as st
from streamlit_extras.colored_header import colored_header
from time import sleep

# 💖 Page setup
st.set_page_config(page_title="Pages for Nay 🩷", page_icon="📖", layout="centered")

# 💜 Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffc5f4, #d7b3ff);
        color: #5a0073;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .book-frame {
        background-color: #fff0fa;
        border: 5px solid #d491ff;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(120, 0, 145, 0.3);
        padding: 30px;
        width: 90%;
        margin: auto;
    }
    .title {
        font-size: 38px;
        text-align: center;
        color: #a00080;
        font-family: 'Brush Script MT', cursive;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #7b007b;
    }
    .nav-btn {
        display: flex;
        justify-content: space-between;
        margin-top: 25px;
    }
    .stButton>button {
        background-color: #ff99dd;
        color: white;
        border-radius: 12px;
        border: none;
        font-size: 18px;
        padding: 10px 25px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d277ff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 💗 Page content
pages = [
    {
        "title": "📖 Pages for Nay 🩷",
        "content": """
        <div style='text-align:center;'>
            <h2 style='font-family:Brush Script MT; font-size:45px;'>Pages for Nay🩷</h2>
            <p style='font-size:20px;'>Made with love by Kate💜</p>
            <p style='font-style:italic;'>Turn the page to begin your little story...</p>
        </div>
        """
    },
    {
        "title": "🎉 Happy Birthday Nay!",
        "content": """
        <p>Hi Nay!!! HAPPY BIRTHDAY TO YOU!!! 🎂💖</p>
        <p>I hope you'll start the day with a smile. It's been months since we started knowing each other — and we still are! I’m so glad that I met a person like you. You’re such a fresh breath of air. I really appreciate you for coming into my life and hopefully, we’ll meet in the future. 🌸</p>
        <p>For now, I hope you enjoy this little gift from me. It’s not much since it’s last minute, but I kept my promise! Anyways, have fun today, and I’m manifesting the TV and giveaway for you. I’ll manifest it hard 😆💫</p>
        <p style='text-align:right; font-style:italic;'>— Love, Kate 💜</p>
        """
    },
    {
        "title": "💬 How We Met",
        "content": """
        <p>Our first “hello” still makes me smile. We just clicked right away — simple messages turned into long talks, laughter, and shared stories. We exchanged Instagram accounts, and from there, our friendship just bloomed. 🌷</p>
        """
    },
    {
        "title": "🐱 The Cat Plushie",
        "content": """
        <p>You sent me a picture of your adorable cat plushie, and guess what? When I was out shopping, I found one that looked just like it! I couldn’t resist — now they’re twins, just like us 🩷💜</p>
        """
    },
    {
        "title": "☕ Girlhood Adventures",
        "content": """
        <p>I imagine us hanging out together — going shopping, visiting a cozy café (maybe a cat café 🐈), painting near the park, baking sweet treats, and laughing about random things. That’s what girlhood means to me — soft moments, warmth, and you in them.</p>
        """
    },
    {
        "title": "🌎 Dream Destinations",
        "content": """
        <p>One day, I’ll visit you in Costa Rica — we’ll explore, eat yummy food, and I’ll learn your language as we make memories. Then, you’ll come to the Philippines and I’ll take you around. We’ll go for walks, sunsets, and laughter — just endless fun and peace.</p>
        <p style='text-align:center;'>🌸 Once it’s all over, we’ll look back and say, “We really did that.” 🌸</p>
        """
    },
    {
        "title": "💌 Thank You",
        "content": """
        <p>Thank you for being my friend, Nay. For being genuine, funny, and kind. This little book is just a small token of how grateful I am for you.</p>
        <p style='text-align:center; font-family:Brush Script MT; font-size:24px;'>Happy Birthday Again! 💕</p>
        """
    }
]

# 🩷 Page flip logic
if "page_num" not in st.session_state:
    st.session_state.page_num = 0

page = pages[st.session_state.page_num]

st.markdown("<div class='book-frame'>", unsafe_allow_html=True)
st.markdown(f"<div class='title'>{page['title']}</div>", unsafe_allow_html=True)
st.markdown(page['content'], unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Navigation
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅ Previous") and st.session_state.page_num > 0:
        st.session_state.page_num -= 1
with col2:
    if st.button("Next ➡") and st.session_state.page_num < len(pages) - 1:
        st.session_state.page_num += 1

# Footer
st.markdown("<br><hr><center><p style='color:#7b007b;'>Made with 💜 by Kate | For Nay’s Birthday 🎀</p></center>", unsafe_allow_html=True)
