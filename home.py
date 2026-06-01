import streamlit as st
from streamlit_lottie import st_lottie
import requests


def show():

    # ---------------- LOTTIE ----------------
    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_home = load_lottie("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

    # ---------------- SIDEBAR (ONLY HOME) ----------------
    st.sidebar.markdown("### 📎 Project Info")
    st.sidebar.info("Final Year ML Project\n\nCrime Prediction & Analysis System")

    st.sidebar.markdown("### 👨‍💻 Developer")
    st.sidebar.write("Your Name")

    # ---------------- BACKGROUND + HERO ----------------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(14,17,23,0.85), rgba(14,17,23,0.95)),
        url("https://images.unsplash.com/photo-1508385082359-f38ae991e8f2");
        background-size: cover;
        background-position: center;
    }

    .hero {
        text-align: center;
        padding: 60px 20px;
    }

    .title {
        font-size: 55px;
        font-weight: bold;
        color: #00c6ff;
    }

    .subtitle {
        font-size: 22px;
        color: #e5e7eb;
        margin-top: 10px;
    }

    .cta-button button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 200px;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- HERO SECTION ----------------
    st.markdown('<div class="hero">', unsafe_allow_html=True)

    st.markdown('<div class="title">🚔 Crime Intelligence System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered crime prediction, analytics & geospatial insights</div>', unsafe_allow_html=True)

    # 🎬 Animation
    st_lottie(lottie_home, height=250)

    # 🚀 BUTTON
    if st.button("🚀 Go to Dashboard"):
        st.session_state.page = "📊 Dashboard"

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- FEATURES ----------------
    st.subheader("✨ Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Data", "50K+ Records")
        st.caption("Large dataset for analysis")

    with col2:
        st.metric("🤖 Model", "XGBoost")
        st.caption("High accuracy ML model")

    with col3:
        st.metric("🗺️ Clusters", "5 Regions")
        st.caption("Geospatial clustering")

    st.markdown("---")

    # ---------------- DESCRIPTION ----------------
    st.subheader("🔍 About System")

    st.markdown("""
    This system helps:
    
    - 📊 Analyze crime patterns  
    - 🤖 Predict crime types  
    - 🗺️ Visualize hotspots  
    - 📈 Generate insights for decision-making  
    """)

    st.markdown("---")

    st.success("👉 Use the sidebar or button above to explore the dashboard 🚀")