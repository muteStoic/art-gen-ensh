import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.write("test")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
userDb = conn.read(
    spreadsheet ="https://docs.google.com/spreadsheets/d/1QIbtWBhbykxaEGtE3bb_vFz5yGnyiUF6Lll1S_IdhCc/edit?usp=sharing")

dff = userDb.at[2,"name"]








st.dataframe(userDb)

st.write(dff)
st.dataframe(df)

userid = st.text_input("idLabel")



