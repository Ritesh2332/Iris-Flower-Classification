import streamlit as st
import numpy as np
import pickle
import os

# Page config
st.set_page_config(page_title="Iris Flower Predictor", page_icon="🌸", layout="centered")

# ---------- UI STYLING ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

h1 {
    text-align: center;
}

.stNumberInput input {
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
    color: white;
}

.stButton>button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 10px;
    padding: 10px;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.05);
}

.result-box {
    padding: 15px;
    border-radius: 12px;
    background: rgba(34,197,94,0.2);
    border: 1px solid rgba(34,197,94,0.5);
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- MODEL LOADING ----------
_MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
if not os.path.exists(_MODEL_PATH):
    raise FileNotFoundError(f"Model not found at: {_MODEL_PATH}")

with open(_MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ---------- HEADER ----------
st.markdown("<h1>Iris Flower Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Enter the flower measurements below</p>", unsafe_allow_html=True)

# ---------- INPUT LAYOUT (2 columns) ----------
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length", 4.0, 8.0, 5.1)
    sepal_width = st.number_input("Sepal Width", 2.0, 4.5, 3.5)

with col2:
    petal_length = st.number_input("Petal Length", 1.0, 7.0, 1.4)
    petal_width = st.number_input("Petal Width", 0.1, 2.5, 0.2)

# ---------- PREDICTION ----------
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)

    species = ["Setosa", "Versicolor", "Virginica"]

    pred0 = prediction[0]
    if isinstance(pred0, (int, np.integer)):
        label = species[int(pred0)]
    else:
        label = str(pred0)

    # Result box
    st.markdown(
        f"<div class='result-box'>Estimated species: <b>{label}</b></div>",
        unsafe_allow_html=True
    )