import streamlit as st
import hashlib

def get_user_and_pass():
    global username, password
    pw = hashlib.md5(password)

    return username, pw


st.header("Login Page")
st.text("\n\n")

username = st.text_input("User: ")
st.text("")
password = st.text_input("Password: ", type="password")
st.text("")

col1, col2 = st.columns(2)
login_bt = col1.button("<Login>")
signin_bt = col2.button("<Sign in>")

if login_bt:
    st.text("hello!")
    st.text(get_user_and_pass())
if signin_bt:
    st.text("sign in")