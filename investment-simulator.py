import streamlit as st
import numpy as np

st.title("🚀 AI Project Investment Simulator")

st.write("Simulate the return on investment of an Artificial Intelligence project")

# Inputs
investment = st.slider("💰 Initial Investment (€)", 10000, 1000000, 100000)
risk = st.selectbox("⚠️ Risk Level", ["Low", "Medium", "High"])
years = st.slider("⏳ Project Duration (years)", 1, 10, 3)
adoption = st.slider("📈 Expected Adoption Level (%)", 10, 100, 50)

# Risk factor
risk_factor = {"Low": 0.9, "Medium": 0.7, "High": 0.5}

# ROI calculation
expected_return = investment * (adoption / 100) * years * risk_factor[risk]
roi = expected_return - investment

st.metric("📊 Estimated ROI (€)", f"{roi:,.0f}")
