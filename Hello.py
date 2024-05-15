import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

if 'validUser' not in st.session_state:
    st.session_state.validUser = False

if 'user' not in st.session_state:
    st.session_state.user = ""

if not st.session_state.validUser:
    with st.sidebar:
        st.write("Please Log in") 

else:
    with st.sidebar:
        st.write(st.session_state.user)




# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)


userDb = conn.read(
    spreadsheet ="https://docs.google.com/spreadsheets/d/1Y5oaJN_XDAy6iM7yVAKKqIofI1WICOmYKWCD3OVQ8E0/edit?usp=sharing",
    usecols = [0,1,2,3]
    )


userid = st.text_input("User Id")

userpwd = st.text_input("User Password")

if st.button("Login"):
    
    if userid == userDb.at[0,"id"]:
        username = "Log in successful. Welcome " + str(userDb.at[0,"id"])
        #st.write(username)
        
        if userpwd == str(userDb.at[0,"password"]):
            password = "the pwd is correct:" + str(userDb.at[0,"password"])
            #st.write(password)
            st.session_state.validUser = True
            st.session_state.user = str(userDb.at[0,"id"])
            st.write("Login successful , welcome " + str(userDb.at[0,"id"]))
        else:
            st.write("incorrect password")
    elif userid == userDb.at[1,"id"]:
        username = "Log in successful. Welcome " + str(userDb.at[1,"id"])
        st.write(username)
        
        if userpwd == str(userDb.at[1,"password"]):
            password = "the pwd is correct:" + str(userDb.at[1,"password"])
            #st.write(password)
            st.session_state.validUser = True
            st.session_state.user = str(userDb.at[1,"id"])
            st.write("Login successful , welcome " + str(userDb.at[1,"id"]))
        else:
            st.write("incorrect password")
    elif userid == userDb.at[2,"id"]:
        username = "Log in successful. Welcome " + str(userDb.at[2,"id"])
        
        if userpwd == str(userDb.at[2,"password"]):
            password = "the pwd is correct:" + str(userDb.at[2,"password"])
            #st.write(password)
            st.session_state.validUser = True
            st.session_state.user = str(userDb.at[2,"id"])
            st.write("Login successful , welcome " + str(userDb.at[2,"id"]))
        else:
            st.write("incorrect password")
    else:
        st.session_state.validUser = False
        st.write("No user found")
    