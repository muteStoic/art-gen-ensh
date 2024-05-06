import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.write("test")
st.write("test2")
st.write("test33")
st.write("test4")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
singlecell = conn.read(usecols = [0])

dff = pd.DataFrame({df})

st.write(dff)

st.write(cell_val)

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

st.dataframe(df)
st.write(singlecell)