import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.write("testingggg")

if 'loginId' not in st.session_state:
    st.session_state.loginId = ""

if 'loginPwd' not in st.session_state:
    st.session_state.loginPwd = ""

if 'loginStatus' not in st.session_state:
    st.session_state.loginStatus = False

status = ""
@st.experimental_dialog("Log in to continue")
def login():
    st.session_state.loginId = st.text_input("User ID")
    st.session_state.loginPwd = st.text_input("User Password")

    if st.button("Login"):
        if st.session_state.loginId == "asd":
            status = "username correct"
            if st.session_state.loginPwd == "123":
                status = "password correct"
                st.session_state.loginStatus = True
                st.rerun()
            else:
                status = "password incorrect"
                st.rerun()
        else:
            status = "username incorrect"
        st.rerun()
    

    

    
if st.session_state.loginStatus == False:
    login()
else:
    st.write(st.session_state.loginStatus)