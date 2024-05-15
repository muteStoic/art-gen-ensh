import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.write("testingggg")

if 'loginId' not in st.session_state:
    st.session_state.loginId = ""

if 'loginPwd' not in st.session_state:
    st.session_state.loginPwd = ""

if 'loginstatus' not in st.session_state:
    st.session_state.loginstatus = False

status = ""
@st.experimental_dialog("Log in to continue")
def login():
    st.session_state.loginId = st.text_input("User ID")
    st.session_state.loginPwd = st.text_input("User Password")

    if st.button("Login"):
        if st.session_state.loginID == "asd":
            status = "username correct"
            if st.session_state.loginPWD == "123":
                status = "password correct"
                st.session_state.loginstatus = True
            else:
                status = "password incorrect"
        else:
            status = "username incorrect"
        st.rerun()
    

    

    
if st.session_state.loginstatus == False:
    login()
else:
    st.write(st.session_state.loginstatus)