import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

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
        


