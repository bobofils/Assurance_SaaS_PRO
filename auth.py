import streamlit as st
from database import create_user, get_user
from security import check_password

def auth_page():

    st.title("🔐 Authentification SaaS")

    menu = st.radio("Menu", ["Login", "Signup"])

    if menu == "Signup":
        user = st.text_input("Utilisateur")
        pwd = st.text_input("Mot de passe", type="password")

        if st.button("Créer compte"):
            if create_user(user, pwd):
                st.success("Compte créé ✅")
            else:
                st.error("Utilisateur existe ❌")

    else:
        user = st.text_input("Utilisateur")
        pwd = st.text_input("Mot de passe", type="password")

        if st.button("Login"):
            data = get_user(user)

            if data and check_password(pwd, data[2]):
                st.session_state["user"] = user
                st.session_state["plan"] = data[4]
                st.session_state["usage"] = data[5]
                st.success("Connexion OK ✅")
                st.rerun()
            else:
                st.error("Erreur login ❌")