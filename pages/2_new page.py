import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.write("test")
st.write("test2")


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.dataframe(df)