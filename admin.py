import streamlit as st
import pandas as pd
from database import get_clients

def admin_dashboard():
    st.subheader("📊 Dashboard Admin")

    data = get_clients()
    df = pd.DataFrame(data, columns=[
        "ID","User","Age","Revenu","Couverture","Risque","Prime","Date"
    ])

    st.dataframe(df)

    if not df.empty:
        st.metric("Total clients", len(df))
        st.metric("Total primes", df["Prime"].sum())
        st.bar_chart(df["Risque"])