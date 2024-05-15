import streamlit as st
from streamlit_gsheets import GSheetsConnection

if not st.session_state.validUser:
    st.warning("Require user to login before proceding. Please head to the 'Log In Page' at the sidebar to log in")
    st.stop()

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="Sheet1")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
