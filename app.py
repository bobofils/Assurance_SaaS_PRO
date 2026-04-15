import streamlit as st
import numpy as np
import pandas as pd
import io
from fpdf import FPDF

from auth import auth_page
from database import init_users, save_client, get_clients
from utils import load_model
from admin import admin_dashboard

init_users()
model = load_model()

st.set_page_config(page_title="Assurance SaaS PRO", layout="wide")

if "user" not in st.session_state:
    auth_page()
    st.stop()

st.title("🛡️ Assurance SaaS PRO")

st.sidebar.success(f"User: {st.session_state['user']}")
st.sidebar.info(f"Plan: {st.session_state.get('plan','free')}")

if st.sidebar.button("Logout"):
    del st.session_state["user"]
    st.rerun()

# =====================
# FORMULAIRE
# =====================
st.header("👤 Client")

age = st.slider("Âge", 18, 80, 30)
revenu = st.number_input("Revenu", 0, 10000000, 300000)
couverture = st.number_input("Couverture", 0, 50000000, 1000000)
anciennete = st.number_input("Ancienneté", 0, 40, 2)
charges = st.number_input("Charges", 0, 5000000, 0)
credit = st.number_input("Crédit", 0, 5000000, 0)

revenu_total = revenu

if st.button("Analyser"):

    X = np.array([[age, revenu_total, couverture, anciennete, charges, credit]])

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]

    risk = round((1 - proba) * 100, 2)

    coef = 0.02 if risk < 30 else 0.05 if risk < 60 else 0.1
    prime = couverture * coef

    st.metric("Risque", f"{risk}%")

    st.success(f"Prime: {prime:,.0f}")

    save_client(age, revenu_total, couverture, risk, prime)

# =====================
# ADMIN
# =====================
st.header("📊 Dashboard")
admin_dashboard()