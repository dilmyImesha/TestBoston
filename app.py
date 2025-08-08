# ---------- Centered Button ----------
st.markdown("### Predict the Price")

# Use HTML to center the button
centered_button = """
    <div style='text-align: center;'>
        <form action='#' method='post'>
            <input type='submit' value='Predict House Price' style='
                background-color: #4a90e2;
                color: white;
                padding: 10px 24px;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                cursor: pointer;
            '>
        </form>
    </div>
"""
st.markdown(centered_button, unsafe_allow_html=True)

# Use st.form to handle submit
with st.form(key='prediction_form', clear_on_submit=False):
    submitted = st.form_submit_button(label="Predict House Price")
    if submitted:
        try:
            prediction = model.predict(input_data)[0]
            st.markdown(
                f"<div class='prediction-box'>Predicted House Price: ${prediction * 1000:.2f}</div>",
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Prediction failed: {e}")
