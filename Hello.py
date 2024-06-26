import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

if 'validUser' not in st.session_state:
    st.session_state.validUser = False

if 'user' not in st.session_state:
    st.session_state.user = ""

if 'tokenUsed' not in st.session_state:
    st.session_state.tokenUsed = ""

if 'userLoc' not in st.session_state:
    st.session_state.userLoc = 0





# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)


userDb = conn.read(
    spreadsheet ="https://docs.google.com/spreadsheets/d/1Y5oaJN_XDAy6iM7yVAKKqIofI1WICOmYKWCD3OVQ8E0/edit?usp=sharing",
    worksheet="Sheet3" ,usecols = [0,1,2,3,4]
    )

#st.write(str(int(userDb.at[2,"token"])))

##section for the sidebar
if not st.session_state.validUser:
    with st.sidebar:
        st.write("Please Log in") 
        st.cache_data.clear()

else:
    with st.sidebar:
        st.write("User: " + str(st.session_state.user))
        st.write("Token used: " + str(int(st.session_state.tokenUsed)))

userid = st.text_input("User Id")

userpwd = st.text_input("User Password")

number_of_users = 2

if st.button("Login"):
    

    """
    for nou in number_of_users:
        if userid == userDb.at[nou,"id"]:
            username = "Log in successful. Welcome " + str(userDb.at[nou,"id"])
            #st.write(username)
            
            if userpwd == str(userDb.at[nou,"password"]):
                password = "the pwd is correct:" + str(userDb.at[nou,"password"])
                #st.write(password)
                st.session_state.validUser = True
                st.session_state.user = str(userDb.at[nou,"id"])
                st.write("Login successful , welcome " + str(userDb.at[nou,"id"]))
                st.session_state.tokenUsed = userDb.at[nou,"token"]
                time.sleep(3)
                st.switch_page("pages/6_Main Page.py")
            else:
                st.write("incorrect password")
        else:
            st.session_state.validUser = False
            st.write("No user found")
            """

        

    
    if userid == userDb.at[0,"id"]:
        username = "Log in successful. Welcome " + str(userDb.at[0,"id"])
        #st.write(username)
        
        if userpwd == str(userDb.at[0,"password"]):
            password = "the pwd is correct:" + str(userDb.at[0,"password"])
            #st.write(password)
            st.session_state.validUser = True
            st.session_state.user = str(userDb.at[0,"id"])
            st.write("Login successful , welcome " + str(userDb.at[0,"id"]))
            st.session_state.tokenUsed = userDb.at[0,"token"]
            st.session_state.userLoc = 0
            time.sleep(3)
            st.switch_page("pages/6_Main Page.py")
        else:
            st.write("incorrect password")
    elif userid == userDb.at[1,"id"]:
        username = "Log in successful. Welcome " + str(userDb.at[1,"id"])
        #st.write(username)
        
        if userpwd == str(userDb.at[1,"password"]):
            password = "the pwd is correct:" + str(userDb.at[1,"password"])
            #st.write(password)
            st.session_state.validUser = True
            st.session_state.user = str(userDb.at[1,"id"])
            st.write("Login successful , welcome " + str(userDb.at[1,"id"]))
            st.session_state.tokenUsed = userDb.at[1,"token"]
            st.session_state.userLoc = 1
            time.sleep(3)
            st.switch_page("pages/6_Main Page.py")
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
            st.session_state.tokenUsed = userDb.at[2,"token"]
            st.session_state.userLoc = 2
            time.sleep(3)
            st.switch_page("pages/6_Main Page.py")
        else:
            st.write("incorrect password")
    else:
        st.session_state.validUser = False
        st.write("No user found")
        
    