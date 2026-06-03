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

    # 🔥 DIFFERENT ANIMATIONS
    lottie_ai = load_lottie("https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json")
    lottie_backend = load_lottie("https://assets2.lottiefiles.com/packages/lf20_xvrofzfk.json")
    lottie_ml = load_lottie("https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json")
    lottie_viz = load_lottie("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")

    # ---------------- STYLE ----------------
    st.markdown("""
    <style>

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #00c6ff;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #aaa;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 25px rgba(0,0,0,0.3);
        transition: 0.3s;
        height: 100%;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(0,198,255,0.6);
    }

    .card-title {
        font-size: 20px;
        font-weight: bold;
        color: #00c6ff;
        margin-bottom: 10px;
    }

    .footer-box {
        margin-top: 30px;
        padding: 20px;
        border-radius: 12px;
        background: rgba(0, 198, 255, 0.1);
        text-align: center;
        color: #00c6ff;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- HEADER ----------------
    st.markdown('<div class="title">ℹ️ About CrimeVision AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered Crime Prediction & Geospatial Intelligence System</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- HERO SECTION ----------------
    col1, col2 = st.columns([1, 2])

    with col1:
        st_lottie(lottie_ai, height=200)

    with col2:
        st.markdown("""
        ### 🚀 Project Overview
        
        This system uses **Machine Learning + Data Analytics** to:
        
        - Predict crime types 📊  
        - Identify crime hotspots 🗺️  
        - Analyze patterns over time ⏱️  
        
        Built as a **real-world intelligent analytics system**.
        """)

    st.markdown("---")

    # ---------------- FEATURES ----------------
    st.markdown("### 🔥 Core Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-title">📊 Data Analysis</div>
            Large-scale dataset exploration to uncover crime trends.
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-title">🤖 ML Prediction</div>
            Predict crime type using trained ML model.
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-title">🗺️ Clustering</div>
            Identify geographical crime hotspots.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- ARCHITECTURE ----------------
    st.markdown("### 🧠 Project Architecture")

    st.markdown("""
    <div class="card">
    
    📂 Dataset (200K Records)  
    ↓  
    🧹 Data Preprocessing (Cleaning, Encoding)  
    ↓  
    🤖 ML Model (XGBoost / Random Forest)  
    ↓  
    💾 Model Saving (.pkl files)  
    ↓  
    🚀 Streamlit Dashboard  
    ↓  
    📊 Visualization + Prediction + Insights  
    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- TECH STACK ----------------
    st.markdown("### ⚙️ Technologies Used")

    col4, col5, col6 = st.columns(3)

    with col4:
        st_lottie(lottie_backend, height=120)
        st.markdown("""
        **Backend**  
        - Python  
        - Pandas  
        - NumPy  
        """)

    with col5:
        st_lottie(lottie_ml, height=120)
        st.markdown("""
        **Machine Learning**  
        - Scikit-learn  
        - XGBoost  
        """)

    with col6:
        st_lottie(lottie_viz, height=120)
        st.markdown("""
        **Frontend & Viz**  
        - Streamlit  
        - Seaborn  
        - Matplotlib  
        """)

    st.markdown("---")

    # ---------------- DEVELOPER ----------------
    st.markdown("### 👨‍💻 Developed By")

    st.markdown("""
    <div class="card">
        Final Year Computer Science Project <br><br>
        Focused on applying Machine Learning to real-world crime analytics.
    </div>
    """, unsafe_allow_html=True)

    # ---------------- FOOTER ----------------
    st.markdown("""
    <div class="footer-box">
    ⚠️ This system is for educational and analytical purposes only.
    </div>
    """, unsafe_allow_html=True)