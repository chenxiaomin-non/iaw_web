import streamlit as st

st.header("Login Page")
st.text("\n\n")

st.text_input("User: ")
st.text("")
st.text_input("Password: ")
st.text("")

if st.button("<Login>"):
    st.text("hello!")
if st.button("<Sign in>"):
    st.text("sign in")