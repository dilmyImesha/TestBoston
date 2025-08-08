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
    body {
        background-color: #f0f6ff;
    }
    .main {
        background-color: #f0f6ff;
        padding: 20px;
    }
    h1 {
        color: #1b4f72;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .prediction-box {
        padding: 20px;
        background-color: #d6eaf8;
        border-left: 5px solid #2980b9;
        border-radius: 10px;
        color: #154360;
        font-size: 20px;
        text-align: center;
        margin-top: 30px;
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

# ---------- Prediction ----------
st.markdown("### Predict the Price")

if st.button("Predict House Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.markdown(
            f"<div class='prediction-box'>Predicted House Price: ${prediction * 1000:.2f}</div>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Prediction failed: {e}")
