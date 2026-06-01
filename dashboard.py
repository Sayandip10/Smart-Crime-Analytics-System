import streamlit as st
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests


def show():

    # ---------------- LOTTIE ----------------
    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_crime = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

    # ---------------- PANEL STATE ----------------
    if "panel_open" not in st.session_state:
        st.session_state.panel_open = True

    if st.button("⚙️ Toggle Control Panel"):
        st.session_state.panel_open = not st.session_state.panel_open

    # ---------------- UI STYLE ----------------
    st.markdown("""
    <style>

    h1 {
        text-align: center;
        color: #00c6ff;
    }

    .floating-panel {
        position: sticky;
        top: 20px;
        background: rgba(255,255,255,0.08);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        animation: slideIn 0.4s ease;
    }

    @keyframes slideIn {
        from { transform: translateX(40px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- HEADER ----------------
    st.markdown("<h1>🚔 Crime Intelligence Dashboard</h1>", unsafe_allow_html=True)
    st_lottie(lottie_crime, height=150)
    st.markdown("---")

    # ---------------- LOAD DATA ----------------
    model = pickle.load(open("crime_model.pkl", "rb"))
    le_type = pickle.load(open("le_type.pkl", "rb"))
    le_area = pickle.load(open("le_area.pkl", "rb"))

    df = pd.read_csv("sample_data.csv")
    df = df.dropna(subset=['latitude', 'longitude'])

    # ---------------- LAYOUT ----------------
    if st.session_state.panel_open:
        main_col, right_col = st.columns([3, 1])
    else:
        main_col = st.container()

    # ================= RIGHT PANEL =================
    if st.session_state.panel_open:
        with right_col:

            st.markdown('<div class="floating-panel">', unsafe_allow_html=True)

            st.subheader("🎛️ Control Panel")
            st.success("🟢 System Active")

            area = st.selectbox("Select Area", le_area.classes_)
            lat = st.number_input("Latitude", value=49.25)
            lon = st.number_input("Longitude", value=-123.12)
            hour = st.slider("Hour", 0, 23)
            use_full_data = st.checkbox("Show Full Dataset", value=False)

            st.markdown('</div>', unsafe_allow_html=True)

    else:
        area = le_area.classes_[0]
        lat = 49.25
        lon = -123.12
        hour = 12
        use_full_data = True

    # ================= MAIN CONTENT =================
    with main_col:

        # 🔥 Subtle loading bar (instant)
        progress = st.progress(0)
        progress.progress(100)
        progress.empty()

        area_encoded = le_area.transform([area])[0]

        # ---------------- FILTER (NO DELAY) ----------------
        if use_full_data:
            filtered_df = df
        else:
            filtered_df = df.copy()
            filtered_df = filtered_df[filtered_df['neighbourhood'] == area]
            filtered_df = filtered_df[
                (filtered_df['hour'] >= hour - 1) &
                (filtered_df['hour'] <= hour + 1)
            ]

        # ---------------- TABS ----------------
        tab1, tab2, tab3 = st.tabs(["📊 Overview", "🗺️ Map & Clusters", "🤖 Prediction"])

        # ===== TAB 1 =====
        with tab1:

            colA, colB, colC = st.columns(3)

            colA.metric("Total Crimes", len(filtered_df))
            colB.metric("Unique Areas", filtered_df['neighbourhood'].nunique())
            colC.metric("Crime Types", filtered_df['type'].nunique())

            st.markdown("---")

            if len(filtered_df) > 0:
                st.bar_chart(filtered_df['type'].value_counts().head(10))

                hour_data = filtered_df['hour'].value_counts().sort_index()
                st.line_chart(hour_data)

        # ===== TAB 2 =====
        with tab2:

            if len(filtered_df) > 0:
                st.map(filtered_df[['latitude', 'longitude']])

                fig, ax = plt.subplots()
                sns.scatterplot(
                    x=filtered_df['longitude'],
                    y=filtered_df['latitude'],
                    hue=filtered_df['cluster'],
                    palette='viridis',
                    ax=ax
                )
                st.pyplot(fig)

        # ===== TAB 3 =====
        with tab3:

            if st.button("Predict Crime"):

                input_data = np.array([[area_encoded, lat, lon, hour]])
                prediction = model.predict(input_data)
                crime_type = le_type.inverse_transform(prediction)

                st.success(f"🚨 Predicted Crime: {crime_type[0]}")
                st.toast("Prediction Complete 🚔")
                st.balloons()

            st.markdown("---")

            col3, col4 = st.columns(2)

            with col3:
                if len(filtered_df) > 0:
                    st.write(filtered_df['neighbourhood'].value_counts().head(5))

            with col4:
                if len(filtered_df) > 0:
                    st.bar_chart(filtered_df['hour'].value_counts().sort_index())