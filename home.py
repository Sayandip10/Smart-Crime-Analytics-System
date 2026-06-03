import streamlit as st
from streamlit_lottie import st_lottie
import requests


def show():

    # ---------------- LOAD LOTTIE ----------------
    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_home = load_lottie("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

    # ---------------- SIDEBAR ----------------
    st.sidebar.markdown("### 📎 Project Info")
    st.sidebar.info("Final Year ML Project\n\nCrime Prediction & Analysis System")

    st.sidebar.markdown("### 👨‍💻 Developer")
    st.sidebar.write("Sayandip Roy")

    # ---------------- STYLE + ANIMATION ----------------
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
        padding: 80px 20px;
    }

    .typing {
        font-size: 60px;
        font-weight: bold;
        color: #00c6ff;
        border-right: 3px solid #00c6ff;
        white-space: nowrap;
        overflow: hidden;
        width: 0;
        animation: typing 3s steps(30, end) forwards, blink 0.7s infinite;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink {
        50% { border-color: transparent }
    }

    .subtitle {
        font-size: 22px;
        color: #e5e7eb;
        margin-top: 10px;
        opacity: 0;
        animation: fadeIn 2s ease forwards;
        animation-delay: 2s;
    }

    .fade-in {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1s ease forwards;
    }

    @keyframes fadeUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 25px rgba(0,0,0,0.3);
        text-align: center;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(0,198,255,0.6);
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- HERO ----------------
    st.markdown('<div class="hero">', unsafe_allow_html=True)

    st.markdown('<div class="typing">🚔 Crime Intelligence System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered crime prediction, analytics & geospatial insights</div>', unsafe_allow_html=True)

    st_lottie(lottie_home, height=260)

    if st.button("🚀 Explore Dashboard"):
        st.session_state.page = "📊 Dashboard"

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- FEATURES ----------------
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### ✨ Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📊 Data Analysis</h3>
            Analyze 200K+ crime records to discover patterns.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🤖 ML Prediction</h3>
            Predict crime types using trained ML models.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🗺️ Geo Insights</h3>
            Visualize crime hotspots using clustering.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- STATS ----------------
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### 📊 System Highlights")

    s1, s2, s3 = st.columns(3)

    s1.metric("📊 Dataset", "200K+ Records")
    s2.metric("🤖 Model", "XGBoost")
    s3.metric("🗺️ Clusters", "5 Regions")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # # ---------------- DEMO VIDEO ----------------
    # st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    # st.markdown("### 🎬 Demo Preview")

    # st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # 👉 replace with your project video

    # st.markdown('</div>', unsafe_allow_html=True)

    # st.markdown("---")

    # ---------------- DESCRIPTION ----------------
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### 🔍 What This System Does")

    st.markdown("""
    - 📊 Analyze crime patterns across regions  
    - 🤖 Predict crime types based on location & time  
    - 🗺️ Identify high-risk zones  
    - 📈 Generate actionable insights  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.success("👉 Click 'Explore Dashboard' to start analyzing 🚀")