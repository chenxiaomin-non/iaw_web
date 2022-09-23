import streamlit as st
import hashlib
import base64

def get_user_and_pass():
    global username, password
    pw = hashlib.md5(bytes(password, encoding='utf-8')).digest()
    pw = base64.b16encode()
    pw = str(pw)
    return username, pw


st.header("Login Page")
st.text("\n\n")

username = st.text_input("User: ")
st.text("")
password = st.text_input("Password: ", type="password")
st.text("")

col1, col2, col3, col4 = st.columns(5)
login_bt = col2.button("<Login>")
signin_bt = col4.button("<Sign in>")

if login_bt:
    st.text("hello!")
    st.text(get_user_and_pass())
if signin_bt:
    st.text("sign in")