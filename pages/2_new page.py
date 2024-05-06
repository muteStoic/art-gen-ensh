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
#df2 = conn.read(worksheet = "Sheet3")
singlecell = conn.read(usecols = [0])

dff = pd.DataFrame({singlecell})

id_loc = dff.at[3,"name"]

#st.write(id_loc)



for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

st.dataframe(df)
st.write(singlecell)