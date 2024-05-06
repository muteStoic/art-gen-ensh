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
df2 = conn.read("Sheet3")
singlecell = conn.read(usecols = [0])

dff = pd.DataFrame({conn})

id_loc = df2.at[3,"id"]

st.write(id_loc)



for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

st.dataframe(df)
st.write(singlecell)