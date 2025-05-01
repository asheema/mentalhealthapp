import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

# Load Lottie animation from URL
#def load_lottie_url(url: str):
    #r = requests.get(url)
    #if r.status_code != 200:
        #return None
    #return r.json()

# Page configuration
st.set_page_config(page_title="Mental Health Predictor", page_icon="🧠", layout="centered")

# Load animation
#lottie_mental = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_wzjsybcu.json")

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Predict", "About"],
        icons=["house", "activity", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Home Page
if selected == "Home":
    st.title("🧠 Mental Health Predictor")
    st.subheader("Track and assess your mental wellness with PHQ-9 & GAD-7.")
    #st_lottie(lottie_mental, height=300)
    st.markdown("### Features:")
    st.markdown("- ✅ Predict using PHQ-9 and GAD-7")
    st.markdown("- 🎨 Engaging and animated interface")
    st.markdown("- 📈 Real-time score summary")

# Prediction Page
elif selected == "Predict":
    st.header("📊 Answer the following questions:")

    st.subheader("PHQ-9 (Depression)")
    phq9 = []
    for i in range(1, 10):
        score = st.slider(f"Q{i}. In the last 2 weeks, how often were you bothered by: ...", 0, 3, 1,
                          format="%d (0: Not at all, 3: Nearly every day)")
        phq9.append(score)

    st.subheader("GAD-7 (Anxiety)")
    gad7 = []
    for i in range(1, 8):
        score = st.slider(f"Q{i}. In the last 2 weeks, how often did you feel: ...", 0, 3, 1,
                          format="%d (0: Not at all, 3: Nearly every day)")
        gad7.append(score)

    if st.button("🔍 Predict Mental Health"):
        total_score = sum(phq9) + sum(gad7)
        if total_score <= 9:
            level = "🟢 Mild"
        elif total_score <= 19:
            level = "🟡 Moderate"
        else:
            level = "🔴 Severe"

        st.success(f"Total Score: `{total_score}`")
        st.info(f"Predicted Level: **{level}**")

# About Page
elif selected == "About":
    st.title("ℹ️ About This App")
    st.write("""
    This app helps assess mental health levels based on standardized questionnaires: PHQ-9 and GAD-7.

    - **PHQ-9** measures depression severity  
    - **GAD-7** measures anxiety severity  

    Built using:
    - 🧠 Streamlit
    - 💡 Python
    - ✨ Lottie Animations

    _This is not a clinical diagnostic tool. Please consult a professional if needed._
    """)

# Style metrics
style_metric_cards()
