
import streamlit as st
from openai import OpenAI
import time
import random
import requests
from requests.auth import HTTPBasicAuth

if not st.session_state.validUser:
    st.warning("Require user to login before proceding. Please head to the 'Hello' page at the sidebar to log in")
    st.stop()

    
client = OpenAI()

assistandid = "asst_271d6dtCJd3QxDvSpU1rzYJd"

api_url = "https://www.zenosyne.info/wp-json/wp/v2/posts"

top_text = "What article do you want to generate today?"

username = "roboaut"
password = "HOpI 1u2n j4CP ZTt2 uRwx amFb"
article_status = "publish"


if 'cur_article' not in st.session_state:
    st.session_state.cur_article = []


if 'article_generated' not in st.session_state:
    st.session_state.article_generated = []


if 'ai_generate' not in st.session_state:
    st.session_state.ai_generate = ""

if 'status_check' not in st.session_state:
    st.session_state.status_check = False

if 'timer' not in st.session_state:
    st.session_state.timer = 0


if 'threadid' not in st.session_state:
    st.session_state.threadid = "Generate to create thread id"
 
username = "roboaut"
password = "HOpI 1u2n j4CP ZTt2 uRwx amFb"
article_status = "publish"



def publish():

    post_data = {
    "title": "test title",
    "content": st.session_state.cur_article,
    "status": article_status,

}
    
    print("run function")
    response = requests.post( 
    api_url, 
    auth=HTTPBasicAuth(username, password), 
    json=post_data, 
) 
    return print(response)
 



def buttonstyle_1():

    message = "revise the previou sarticle you generated to be more entertaining and bit more humourous. hide your thinking process and just deliver the revise article."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def buttonstyle_2():

    message = "revise the previous article you have generated to 'Old english' style of writing. "
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()
    

def buttonstyle_3():

    message = "revise the previous article you have generated to follow the new style as follows.  As a creative writer focused on game writing content, I bring humor and an informal style to my responses. I use simple language, avoiding complex words, and employ pop culture references and analogies to make game information both accessible and entertaining. My content is structured as a listicle with clear, catchy headings. I engage readers directly by using a conversational tone, posing questions, and encouraging interaction. I balance detail with brevity . I'm designed to help users understand and enjoy game information through engaging, humorous writing."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def buttonstyle_4():

    message = "Infuse consistent humor throughout your writing, including jokes, witty remarks, and amusing observations to keep it light and engaging. Employ imaginative analogies and metaphors to help the reader visualize and understand concepts in unexpected and memorable ways. Use conversational language that mimics advice from a witty and knowledgeable friend, making the tone informal and accessible. Utilize playful exaggeration for comedic effect, highlighting the absurdities or challenges of the topic in a light-hearted manner. Assign human attributes or behaviors to non-human elements (personification) to make the content more relatable and amusing. Craft an engaging introduction and conclusion with strong, humorous notes, setting a playful tone at the start and concluding with a punchline or insightful amusement at the end. Directly address the reader using 'you' to create a personal and engaging narrative, incorporating humorous asides and rhetorical questions to enhance engagement."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()





def create_thread():
    thread = client.beta.threads.create()
    st.session_state.threadid = thread.id

    return st.session_state.threadid
    




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
    


    
    #while run.status != "completed":
        #time.sleep(1)
        #print(run.status)

    

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread_id=st.session_state.threadid)
        print(messages)

        last_message = messages.data[0]
        response = last_message.content[0].text.value
        print(response)
        st.session_state.article_generated.append(response)
        st.session_state.cur_article = response
        #st.session_state.cur_article = '"""' + st.session_state.cur_article + '"""'
        st.session_state.ai_generate = response
        #ai_generate.append(response)
        

    else:
        
        print(run.status)
        st.toast("Generating Failed. Regenerating Article")

            
        run_open_AI()
            
    #return ai_generate
    



def regen():

    message = "Regenerate again"
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def download_article():
    full_article = "\n\n\n\n".join(st.session_state.article_generated)

    return full_article



def main(message):
    
    st.session_state.article_generated.append(message)

    if st.session_state.threadid == "Generate to create thread id":
        with st.spinner('Creating thread'):
            create_thread()

    with st.spinner('Sending Message'):
        save_message(message)

    with st.spinner('Generating Article'):
        run_open_AI()

    st.session_state.status_check = False

    
            

        #st.session_state.timer = 0
    #processing()
    #ai_generate.append("fasefe")


def main_publish():
    
    


    message = "change the current article to html. make the conversion as just text HTML so i can copy paste it. i just want the <pr>, <br> and etc. i do not need the DOCTYPE info."
    with st.spinner('Sending Message'):
        save_message(message)

    with st.spinner('Generating Article'):
        run_open_AI()

    st.session_state.status_check = False

    publish()
    print("publish done")
            

    


if st.session_state.article_generated == []:
    st.session_state.status_check = True
else:
    st.session_state.status_check = False

  










st.sidebar.success("select page above")


st.header(top_text, divider = "violet")


with st.container():
    col1, col2 = st.columns([7,3])
    with col1: 
        user_request = st.text_area("User Prompt", height = 200)


    with col2: #button
        if st.button("Generate", use_container_width = True):
            main(user_request)
            


        st.divider()
        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            if st.button("Style 1", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_1()

            if st.button("Style 2", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_2()
        with col2:
            if st.button("Style 3", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_3()
            if st.button("Style 4", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_4()




st.divider()

with st.container():
    col1, col2, col3 = st.columns([1,4,4])
    with col1:
        st.write("Status:")


    with col2:
        if st.button("Publish",disabled = st.session_state.status_check, use_container_width = True):
            main_publish()

           

        st.write(st.session_state.threadid)

    with col3:
        st.download_button("Download", data = download_article() , use_container_width = True, disabled = st.session_state.status_check)
        if st.button("New Thread", use_container_width = True,disabled = st.session_state.status_check):
            create_thread()





st.divider()

with st.container(border = None):
     col1, col2 = st.columns([18,4])

     with col1:
        st.subheader("Output")

     with col2:
        if st.button("Regenerate", use_container_width = True,disabled = st.session_state.status_check):
            regen()
            st.session_state.article_generated.append(user_request)



with st.container(border = True):
    #st.write(cache_section())
    
    st.write(st.session_state.ai_generate)


with st.expander("Previous response"):
    with st.container(border = True):
    #st.write(cache_section())
    
        st.write(st.session_state.article_generated)

