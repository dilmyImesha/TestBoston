import streamlit as st
import pickle
import pandas as pd

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 10px;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #2e86de;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .stSidebar {
        background-color: #f1f1f1;
    }
    .prediction-box {
        padding: 20px;
        background-color: #eafaf1;
        border-left: 5px solid #28a745;
        border-radius: 10px;
        color: #1c4532;
        font-size: 20px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Load Model ----------
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# ---------- Title ----------
st.title("Boston Housing Price Prediction")
st.markdown("Enter the values of the features below to predict the house price (in $1000s).")

# ---------- Sidebar Inputs ----------
st.sidebar.header("Input Features")

with st.sidebar.expander("Neighborhood Features"):
    CRIM = st.number_input("Per capita crime rate (CRIM)", 0.0, 100.0, 0.1)
    ZN = st.number_input("Proportion of residential land zoned (ZN)", 0.0, 100.0, 18.0)
    INDUS = st.number_input("Non-retail business acres (INDUS)", 0.0, 30.0, 10.0)
    CHAS = st.selectbox("Charles River proximity (CHAS)", [0, 1])

with st.sidebar.expander("Housing and Pollution"):
    NOX = st.number_input("Nitric oxides concentration (NOX)", 0.0, 1.0, 0.5)
    RM = st.number_input("Average rooms per dwelling (RM)", 1.0, 10.0, 6.0)
    AGE = st.number_input("Older units (%) (AGE)", 0.0, 100.0, 50.0)

with st.sidebar.expander("Accessibility and Tax"):
    DIS = st.number_input("Distance to employment centers (DIS)", 0.0, 15.0, 5.0)
    RAD = st.number_input("Highway accessibility index (RAD)", 1, 24, 4)
    TAX = st.number_input("Property tax rate (TAX)", 100.0, 1000.0, 300.0)

with st.sidebar.expander("Education and Demographics"):
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

# ---------- Predict Button ----------
st.markdown("### Click the button below to get your house price prediction")

if st.button("Predict House Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.markdown(f"<div class='prediction-box'>Predicted House Price: ${prediction * 1000:.2f}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Prediction failed: {e}")
