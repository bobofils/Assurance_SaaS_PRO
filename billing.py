import streamlit as st

def show_billing():

    st.title("💰 Plans Assurance SaaS")

    st.subheader("🆓 Free")
    st.write("- Analyse basique")

    st.subheader("⭐ Pro")
    st.write("- IA complète")
    st.write("- Export PDF/Excel")

    st.subheader("💎 Premium")
    st.write("- API + multi-agents")

    if st.button("Upgrade Pro"):
        st.success("Paiement Stripe à connecter")