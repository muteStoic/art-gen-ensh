import streamlit as st

from streamlit_gsheets import GSheetsConnection

st.write("test database")



# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)