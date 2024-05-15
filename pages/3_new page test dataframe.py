import streamlit as st
from streamlit_gsheets import GSheetsConnection

if not st.session_state.validUser:
    st.warning("Require user to login before proceding. Please head to the 'Log In Page' at the sidebar to log in")
    st.stop()


if not st.session_state.validUser:
    with st.sidebar:
        st.write("Please Log in") 

else:
    with st.sidebar:
        st.write("User: " + str(st.session_state.user))
        st.write("Token used: " + str(int(userDb.at[0,"token"])))

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="Sheet1")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
