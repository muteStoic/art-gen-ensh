import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

if 'userfound' not in st.session_state:
    st.session_state.userfound = False

st.write("test")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
conn2 = st.connection("gsheets2", type=GSheetsConnection)

df = conn.read()
#p12 = conn2.read()

userDb = conn.read(
    spreadsheet ="https://docs.google.com/spreadsheets/d/1QIbtWBhbykxaEGtE3bb_vFz5yGnyiUF6Lll1S_IdhCc/edit?usp=sharing",
    usecols = [0,1,2,3]
    )

dff = userDb.at[0,"name"]

#st.dataframe(p12)


userDb.iloc[4,1] = 50
tokenuse = st.text_input("token use")
if st.button("add token"):
    userDb.iloc[0,3] = tokenuse
    userDb = conn.update(data = userDb)


testdb = st.dataframe(userDb)



st.write(dff)

userid = st.text_input("User Id")

userpwd = st.text_input("User Password")

if st.button("Login"):
    st.write("log in test")
    
    if userid == userDb.at[0,"name"]:
        username = "the user is " + str(userDb.at[0,"name"])
        st.write(username)
        st.session_state.userfound = True
        if userpwd == userDb.at[0,"password"]:
            password = "the pwd is correct:" + str(userDb.at[0,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    elif userid == userDb.at[1,"name"]:
        username = "the user is " + str(userDb.at[1,"name"])
        st.write(username)
        st.session_state.userfound = True
        if userpwd == userDb.at[1,"password"]:
            password = "the pwd is correct:" + str(userDb.at[1,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    elif userid == userDb.at[2,"name"]:
        username = "the user is " + str(userDb.at[2,"name"])
        st.write(username)
        st.session_state.userfound = True
        if userpwd == userDb.at[2,"password"]:
            password = "the pwd is correct:" + str(userDb.at[2,"password"])
            st.write(password)
        else:
            st.write("incorrect password")
    else:
        st.session_state.userfound = False
        st.write("no user found")
    

        


