import streamlit as st
from textwrap import dedent

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pages for Nay 💖", page_icon="📖", layout="centered")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
    body {
        background-color: #fff0f6;
        font-family: 'Poppins', sans-serif;
        color: #4b004b;
    }
    .book-frame {
        background: #fff;
        border: 4px solid #ffb6e6;
        box-shadow: 0px 0px 25px rgba(255, 105, 180, 0.3);
        border-radius: 20px;
        padding: 40px;
        max-width: 600px;
        margin: auto;
        position: relative;
        animation: fadeIn 1.5s ease;
    }
    .book-title {
        text-align: center;
        font-size: 1.8em;
        font-weight: 700;
        color: #d63384;
    }
    .subtitle {
        text-align: center;
        font-size: 1em;
        color: #993399;
        margin-bottom: 25px;
    }
    .secret-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #ff7bc8 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 30px !important;
        font-size: 1em !important;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff47aa !important;
        transform: scale(1.05);
    }
    footer {
        text-align: center;
        font-size: 0.9em;
        color: #b34db3;
        margin-top: 30px;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# --- PAGE DATA ---
pages = [
    {
        "title": "📖 Pages for Nay 💗",
        "text": dedent("""
        Made with love by Kate 💜  

        *Turn the page to begin your little story...*
        """)
    },
    {
        "title": "How We Met 💬",
        "text": dedent("""
        You were the first to say hello on HelloTalk.  
        That same day we moved our chat to Instagram —  
        and I found someone who loves books and cute things just like me.  
        This is where our story began. ✨
        """)
    },
    {
        "title": "Matching Cats 🐱",
        "text": dedent("""
        You sent me a photo of your adorable cat plushie —  
        and when I found one just like it, I knew I had to get it too.  
        Now they’re twins, just like us. 💕
        """)
    },
    {
        "title": "Girlhood Adventures 💄🛍️",
        "text": dedent("""
        Shopping sprees, hanging out at a cat café,  
        painting near the sea, and baking sweet treats together.  
        Every idea feels soft, calm, and full of laughter — our kind of magic.
        """)
    },
    {
        "title": "Dream Destinations 🌍",
        "text": dedent("""
        Someday I’ll visit you in Costa Rica — we’ll explore,  
        learn your language, and enjoy your culture.  
        Then you’ll come with me to the Philippines,  
        where more stories and adventures wait.  
        Until then, this is our little dreambook. 💫
        """)
    },
    {
        "title": "From Kate 💌",
        "text": dedent("""
        Hi Nay!!!  

        Happy birthday — I hope your day begins with a big smile.  
        It’s been months since we started talking, and I’m so grateful we still are.  
        Meeting you felt like a fresh breeze: calm, kind, and bright.  
        Thank you for coming into my life and for being such a warm, gentle friend.  

        I hope we get to meet in person someday, but for now I made you this little storybook.  
        It’s a small, last-minute gift, but I kept my promise.  
        Have so much fun today — I’ll be manifesting that TV and giveaway for you (very hard). 🎁✨  

        Happy birthday again — love you lots!  
        — Kate 💜
        """)
    }
]

# --- PAGE FLIPPING STATE ---
if "page_num" not in st.session_state:
    st.session_state.page_num = 0

def next_page():
    if st.session_state.page_num < len(pages) - 1:
        st.session_state.page_num += 1

def prev_page():
    if st.session_state.page_num > 0:
        st.session_state.page_num -= 1

# --- DISPLAY BOOK FRAME ---
with st.container():
    st.markdown('<div class="book-frame">', unsafe_allow_html=True)
    st.markdown(f"<div class='book-title'>{pages[st.session_state.page_num]['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{pages[st.session_state.page_num]['text']}</div>", unsafe_allow_html=True)

    # Centered navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Previous"):
            prev_page()
    with col3:
        if st.button("Next →"):
            next_page()
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECRET CAT BUTTON ---
st.markdown('<div class="secret-btn">', unsafe_allow_html=True)
if st.button("🐱 Secret Cat"):
    st.balloons()
    st.success("You found the secret cat! Here’s your hidden hug from Kate 🩷🐾")
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<footer>Made with 💜 by Kate | For Nay’s Birthday 🎀</footer>", unsafe_allow_html=True)
