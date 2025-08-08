import streamlit as st
import pickle
import pandas as pd

# ---------- Load Model ----------
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, .main {
        background-image: url("https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }

    .main {
        background-color: rgba(0, 0, 0, 0.5);  /* Overlay */
        padding: 40px;
        border-radius: 15px;
    }

    h1 {
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 700;
    }

    .stNumberInput>div>div>input {
        background-color: #ffffff20 !important;
        color: white !important;
        border-radius: 8px;
    }

    .stSelectbox>div>div>div {
        background-color: #ffffff20 !important;
        color: white !important;
        border-radius: 8px;
    }

    .stButton>button {
        display: block;
        margin: auto;
        background: linear-gradient(90deg, #4a90e2, #357abd);
        color: white;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 10px;
        border: none;
        transition: background 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #357abd, #2c6aa0);
    }

    .prediction-box {
        padding: 25px;
        background-color: rgba(255, 255, 255, 0.8);
        border-left: 8px solid #004080;
        border-radius: 10px;
        color: #002b50;
        font-size: 22px;
        text-align: center;
        margin-top: 30px;
    }

    label, .stMarkdown, .stSelectbox label {
        font-size: 16px !important;
        font-weight: 500;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("Boston Housing Price Prediction")
st.markdown("Enter the values below to predict the house price (in $1000s).")

# ---------- Layout for Input Fields ----------
col1, col2 = st.columns(2)

with col1:
    CRIM = st.number_input("Per capita crime rate (CRIM)", 0.0, 100.0, 0.1)
    ZN = st.number_input("Residential land zoned (ZN)", 0.0, 100.0, 18.0)
    INDUS = st.number_input("Non-retail business acres (INDUS)", 0.0, 30.0, 10.0)
    CHAS = st.selectbox("Charles River proximity (CHAS)", [0, 1])
    NOX = st.number_input("Nitric oxides concentration (NOX)", 0.0, 1.0, 0.5)
    RM = st.number_input("Avg rooms per dwelling (RM)", 1.0, 10.0, 6.0)
    AGE = st.number_input("Older units (%) (AGE)", 0.0, 100.0, 50.0)

with col2:
    DIS = st.number_input("Distance to employment centers (DIS)", 0.0, 15.0, 5.0)
    RAD = st.number_input("Highway access index (RAD)", 1, 24, 4)
    TAX = st.number_input("Property tax rate (TAX)", 100.0, 1000.0, 300.0)
    PTRATIO = st.number_input("Pupil-teacher ratio (PTRATIO)", 10.0, 30.0, 18.0)
    B = st.number_input("Proportion of blacks by town (B)", 0.0, 400.0, 350.0)
    LSTAT = st.number_input("Lower status population (%) (LSTAT)", 0.0, 40.0, 12.0)

# ---------- Input DataFrame ----------
input_data = pd.DataFrame({
    'CRIM': [CRIM],
    'ZN': [ZN],
    'INDUS': [INDUS],
    'CHAS': [CHAS],
    'NOX': [NOX],
    'RM': [RM],
    'AGE': [AGE],
    'DIS': [DIS],
    'RAD': [RAD],
    'TAX': [TAX],
    'PTRATIO': [PTRATIO],
    'B': [B],
    'LSTAT': [LSTAT]
})

# ---------- Prediction Button ----------
st.markdown("### ")
if st.button("Predict House Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.markdown(
            f"<div class='prediction-box'>Predicted House Price: ${prediction * 1000:.2f}</div>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Prediction failed: {e}")
