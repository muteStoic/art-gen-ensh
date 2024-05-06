import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

if 'userfound' not in st.session_state:
    st.session_state.userfound = False

st.write("test")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
userDb = conn.read(
    spreadsheet ="https://docs.google.com/spreadsheets/d/1QIbtWBhbykxaEGtE3bb_vFz5yGnyiUF6Lll1S_IdhCc/edit?usp=sharing")

dff = userDb.at[0,"name"]








st.dataframe(userDb)

st.write(dff)

userid = st.text_input("User Id")

userpwd = st.text_input("User Password")

if st.button("Login"):
    st.write("log in test")
    
    if userid == userDb.at[0,"name"]:
        username = "the user is " + str(userDb.at[0,"name"])
        st.write(username)
        st.session_state.userfound
        if userpwd == userDb.at[0,"password"]:
            password = "the pwd is correct:" + str(userDb.at[0,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    if userid == userDb.at[1,"name"]:
        username = "the user is " + str(userDb.at[1,"name"])
        st.write(username)
        st.session_state.userfound
        if userpwd == userDb.at[1,"password"]:
            password = "the pwd is correct:" + str(userDb.at[1,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    if userid == userDb.at[2,"name"]:
        username = "the user is " + str(userDb.at[2,"name"])
        st.write(username)
        st.session_state.userfound
        if userpwd == userDb.at[2,"password"]:
            password = "the pwd is correct:" + str(userDb.at[2,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    

    if st.session_state.userfound == False:
        st.write("no user found")
        


