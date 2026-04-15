import streamlit as st
from database import get_clients
import pandas as pd

def admin_dashboard():

    st.title("📊 Admin Dashboard")

    data = get_clients()

    df = pd.DataFrame(data, columns=[
        "ID","Age","Revenu","Couverture","Risque","Prime","Date"
    ])

    st.dataframe(df)
    st.bar_chart(df["Risque"])