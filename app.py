import streamlit as st
import time

st.set_page_config(page_title="Crime Dashboard", layout="wide")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# ---------------- LOADER FUNCTION ----------------
def show_loader():
    progress = st.progress(0)
    with st.spinner("Loading page... 🚀"):
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
    progress.empty()

# ---------------- ADVANCED SIDEBAR UI ----------------
st.markdown("""
<style>

/* App Background */
.stApp {
    background: linear-gradient(135deg, #0e1117, #111827);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #020617);
    padding: 20px;
    transition: all 0.4s ease;
}

/* Sidebar collapse animation */
section[data-testid="stSidebar"][aria-expanded="false"] {
    transform: translateX(-10px);
    opacity: 0.9;
}

/* Title */
.sidebar-title {
    font-size: 30px;
    font-weight: bold;
    color: #00c6ff;
    text-align: center;
    margin-bottom: 25px;
}

/* Section Box */
.sidebar-box {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
    transition: all 0.3s ease;
}

/* Hover Glow Effect */
.sidebar-box:hover {
    box-shadow: 0 0 15px rgba(0,198,255,0.5);
    transform: translateY(-3px);
}

/* Radio buttons */
div[role="radiogroup"] > label {
    font-size: 18px !important;
    padding: 10px;
    border-radius: 8px;
    transition: all 0.3s ease;
}

/* Hover effect on nav items */
div[role="radiogroup"] > label:hover {
    background: rgba(0,198,255,0.2);
    box-shadow: 0 0 10px rgba(0,198,255,0.6);
}

/* Active selected item */
div[role="radiogroup"] > label[data-selected="true"] {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white !important;
    box-shadow: 0 0 12px rgba(0,198,255,0.8);
}

/* Toggle spacing */
.stToggle {
    margin-bottom: 15px;
}

/* Footer */
.sidebar-footer {
    position: fixed;
    bottom: 20px;
    font-size: 14px;
    color: gray;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR HEADER ----------------
try:
    st.sidebar.image("logo.png", width=90)
except:
    pass

st.sidebar.markdown('<div class="sidebar-title">🚔 Crime AI</div>', unsafe_allow_html=True)

# ---------------- THEME ----------------
st.sidebar.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
st.sidebar.markdown("### 🎨 Appearance")

theme = st.sidebar.toggle("🌗 Dark Mode", value=True)

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Light mode
if not theme:
    st.markdown("""
    <style>
    .stApp {
        background: white;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.sidebar.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
st.sidebar.markdown("### 📌 Navigation")

pages = ["🏠 Home", "📊 Dashboard", "ℹ️ About"]

if st.session_state.page not in pages:
    st.session_state.page = "🏠 Home"

page = st.sidebar.radio(
    "",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# ---------------- LOADER ----------------
if "last_page" not in st.session_state:
    st.session_state.last_page = st.session_state.page

if st.session_state.page != st.session_state.last_page:
    show_loader()
    st.session_state.last_page = st.session_state.page

# ---------------- FOOTER ----------------
#st.sidebar.markdown(
    #'<div class="sidebar-footer">⚡ Powered by Machine Learning</div>',
    #unsafe_allow_html=True
#)

# ---------------- ROUTING ----------------
if st.session_state.page == "🏠 Home":
    import home
    home.show()

elif st.session_state.page == "📊 Dashboard":
    import dashboard
    dashboard.show()

elif st.session_state.page == "ℹ️ About":
    import about
    about.show()