import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.write("test")
st.write("test2")
st.write("test33")
st.write("test4")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
singlecell = conn.iloc[2,2]



st.dataframe(df)
st.write(singlecell)