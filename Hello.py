import streamlit as st
from openai import OpenAI
import time
import random


client = OpenAI()

top_text = "What article do you want to generate today?"




if 'article_generated' not in st.session_state:
    st.session_state.article_generated = []


if 'ai_generate' not in st.session_state:
    st.session_state.ai_generate = ""



thread_created = 0
assistandid = "asst_271d6dtCJd3QxDvSpU1rzYJd"

if 'threadid' not in st.session_state:
    st.session_state.threadid = "thread_8q5XgvGHNjeMYk2MfJrW4bqh"




def create_thread():
    if thread_created == 0:
        thread = client.beta.threads.create()
        st.session_state.threadid = thread.id
    else:
        print("Thread have created")




def save_message(message):
    message = client.beta.threads.messages.create(
    thread_id=st.session_state.threadid,
    role="user",
    content= message
    )



def run_open_AI():
    run = client.beta.threads.runs.create_and_poll(
    thread_id=st.session_state.threadid,
    assistant_id=assistandid  
    )

    
    while run.status != "completed":
        time.sleep(1)
        print(run.status)

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread_id=st.session_state.threadid)
        print(messages)

        last_message = messages.data[0]
        response = last_message.content[0].text.value
        print(response)
        st.session_state.article_generated.append(response)
        st.session_state.ai_generate = response
        #ai_generate.append(response)
        

    else:
        print(run.status)
    #return ai_generate


def main(message):

    #create_thread()
    save_message(message)
    run_open_AI()
    #processing()
    #ai_generate.append("fasefe")

   
threadtest = st.session_state.threadid    










# Using "with" notation
with st.sidebar:
    st.write("Sidebar section: WIP")


st.header(top_text, divider = "violet")


with st.container():
    col1, col2 = st.columns([7,3])
    with col1: 
        user_request = st.text_area("User Prompt", height = 200)


    with col2: #button
        if st.button("Generate", use_container_width = True):
            main(user_request)
            st.session_state.article_generated.append(user_request)


        st.divider()
        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            st.button("Style 1", use_container_width = True)
            st.button("Style 2", use_container_width = True)
        with col2:
            st.button("Style 3", use_container_width = True)
            st.button("Style 4", use_container_width = True)




st.divider()

with st.container():
    col1, col2, col3 = st.columns([1,4,4])
    with col1:
        st.write("Status:")


    with col2:
        st.status("Running", state = "running")
        st.write(threadtest)

    with col3:
        st.button("Download",use_container_width = True)
        if st.button("New Thread", use_container_width = True):
            create_thread()





st.divider()
st.write("Output")



with st.container(border = True):
    #st.write(cache_section())
    
    st.write(st.session_state.ai_generate)


with st.expander("Previous response"):
    with st.container(border = True):
    #st.write(cache_section())
    
        st.write(st.session_state.article_generated)





