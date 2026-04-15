import streamlit as st
import numpy as np

from auth import auth_page
from database import init_db, save_client, increment_usage
from billing import check_access
from utils import load_model
from admin import admin_dashboard

st.set_page_config(layout="wide")

init_db()
model = load_model()

if "user" not in st.session_state:
    auth_page()
    st.stop()

st.title("🛡️ Assurance SaaS PRO")

user = st.session_state["user"]
plan = st.session_state["plan"]
usage = st.session_state["usage"]

st.sidebar.write(f"👤 {user}")
st.sidebar.write(f"📦 Plan: {plan}")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# LIMIT
if not check_access(plan, usage):
    st.error("🚫 Limite gratuite atteinte. Passe au plan PRO.")
    st.stop()

# FORM
age = st.slider("Âge", 18, 80)
revenu = st.number_input("Revenu", 0, 10000000)
couverture = st.number_input("Couverture", 0, 50000000)

if st.button("Analyser"):
    X = np.array([[age, revenu, couverture]])
    proba = model.predict_proba(X)[0][1]
    risk = (1 - proba) * 100

    prime = couverture * 0.05

    st.metric("Risque", f"{risk:.2f}%")
    st.success(f"Prime: {prime:,.0f} FCFA")

    save_client(user, age, revenu, couverture, risk, prime)
    increment_usage(user)

# ADMIN
if user == "admin":
    admin_dashboard()