import streamlit as st
import requests

st.set_page_config(page_title="House Price Predictor", layout="wide")

st.title("🏠 House Price Prediction")
st.write("Input the variables below to get a prediction:")

# Map the short variable names to their full descriptions
feature_info = {
    'CRIM': "CRIM - per capita crime rate by town",
    'ZN': "ZN - proportion of residential land zoned for lots over 25,000 sq.ft.",
    'INDUS': "INDUS - proportion of non-retail business acres per town.",
    'CHAS': "CHAS - Charles River dummy (1 if tract bounds river; 0 otherwise)",
    'NOX': "NOX - nitric oxides concentration (parts per 10 million)",
    'RM': "RM - average number of rooms per dwelling",
    'AGE': "AGE - proportion of owner-occupied units built prior to 1940",
    'DIS': "DIS - weighted distances to five Boston employment centres",
    'RAD': "RAD - index of accessibility to radial highways",
    'TAX': "TAX - full-value property-tax rate per $10,000",
    'PTRATIO': "PTRATIO - pupil-teacher ratio by town",
    'B': "B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town",
    'LSTAT': "LSTAT - % lower status of the population"
}

user_data = {}

# Use columns to keep the UI organized while using long labels
col1, col2 = st.columns(2)

# Iterate through the dictionary to build the form
for i, (key, full_label) in enumerate(feature_info.items()):
    # Alternates between column 1 and column 2
    with col1 if i % 2 == 0 else col2:
        user_data[key] = st.number_input(
            label=full_label,  # This puts the full text as the heading
            key=key, 
            value=0.0, 
            format="%.5f"
        )

st.divider()

if st.button("🚀 Send to API", use_container_width=True):
    url = "http://127.0.0.1:8000/predict_api"
    try:
        response = requests.post(url, json={"data": user_data})
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Predicted Value: ${result:,.2f}k")
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")