import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.write("test")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
st.dataframe(df)