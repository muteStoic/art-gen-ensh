
import streamlit as st
from openai import OpenAI
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time
import random
import requests
from requests.auth import HTTPBasicAuth




if not st.session_state.validUser:
    st.warning("Require user to login before proceding. Please head to the 'Hello' page at the sidebar to log in")
    st.stop()

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    spreadsheet="https://docs.google.com/spreadsheets/d/1Y5oaJN_XDAy6iM7yVAKKqIofI1WICOmYKWCD3OVQ8E0/edit?usp=sharing"
    ,worksheet="Sheet3", usecols = [0,1,2,3])




print(df.at[0,"token"])
curtoken = df.at[0,"token"]

    
client = OpenAI()

assistandid = "asst_YKTzFq8pYFxpZaWZMi6QzPay"

api_url = "https://www.zenosyne.info/wp-json/wp/v2/posts"

top_text = "What article do you want to generate today?"




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
article_status = "draft"


print("test")
def publish():

    post_data = {
    "title": "test title",
    "content": st.session_state.cur_article,
    "status": "publish",

}
    
    print("run function")
    response = requests.post( 
    api_url, 
    auth=HTTPBasicAuth(username, password), 
    json=post_data, 
) 
    return print(response)

def draft():

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
    message = "Do not greet the reader in the beginning of the article. use the information gathered to craft an article.  As a creative writer focused on game writing content, I bring humor and an informal style to my responses. I use simple language, avoiding complex words, and employ pop culture references and analogies to make game information both accessible and entertaining. My content is structured as a listicle with clear, catchy headings. I engage readers directly by using a conversational tone, posing questions, and encouraging interaction. I balance detail with brevity . I'm designed to help users understand and enjoy game information through engaging, humorous writing."
    #message = "revise the previou sarticle you generated to be more entertaining and bit more humourous. hide your thinking process and just deliver the revise article."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def buttonstyle_2():
    message = "Do not greet the reader in the beginning of the article. Infuse consistent humor throughout your writing, including jokes, witty remarks, and amusing observations to keep it light and engaging. Employ imaginative analogies and metaphors to help the reader visualize and understand concepts in unexpected and memorable ways. Use conversational language that mimics advice from a witty and knowledgeable friend, making the tone informal and accessible. Utilize playful exaggeration for comedic effect, highlighting the absurdities or challenges of the topic in a light-hearted manner. Assign human attributes or behaviors to non-human elements (personification) to make the content more relatable and amusing. Craft an engaging introduction and conclusion with strong, humorous notes, setting a playful tone at the start and concluding with a punchline or insightful amusement at the end. Directly address the reader using 'you' to create a personal and engaging narrative, incorporating humorous asides and rhetorical questions to enhance engagement."
    #message = "revise the previous article you have generated to 'Old english' style of writing. "
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()
    

def buttonstyle_3():
    message = "Revise the previous article you have generated to change the writing style to expository style. Do not greet the reader in the beginning of the article.  Make the article engaging by incorporating anecdotes, examples, and a narrative flow that captures the reader's interest from beginning to end. Infuse the article with light-hearted humor and clever wit to make the content enjoyable and entertaining. Employ vivid and descriptive language to paint a clear picture for the reader, making the information more tangible and easy to visualize."

    #message = "revise the previous article you have generated to follow the new style as follows.  As a creative writer focused on game writing content, I bring humor and an informal style to my responses. I use simple language, avoiding complex words, and employ pop culture references and analogies to make game information both accessible and entertaining. My content is structured as a listicle with clear, catchy headings. I engage readers directly by using a conversational tone, posing questions, and encouraging interaction. I balance detail with brevity . I'm designed to help users understand and enjoy game information through engaging, humorous writing."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def buttonstyle_4():
    message = "Revise the previous article you have generated to change the writing style to blogging style. Do not greet the reader in the beginning of the article.  Infuse the article with light-hearted humor and clever wit to make the content enjoyable and entertaining. Use storytelling techniques: Make the article engaging by incorporating anecdotes, examples, and a narrative flow that captures the reader's interest from beginning to end. Add a bit of humour and wit: Infuse the article with light-hearted humor and clever wit to make the content enjoyable and entertaining. Use descriptive language: Employ vivid and descriptive language to paint a clear picture for the reader, making the information more tangible and easy to visualize. Casual tone: Maintain a friendly and relaxed tone throughout the article, as if you are having a casual conversation with the reader. Simple language complexity: Use simple and straightforward language to ensure the article is easy to understand for a wide audience."
    #message = "Infuse consistent humor throughout your writing, including jokes, witty remarks, and amusing observations to keep it light and engaging. Employ imaginative analogies and metaphors to help the reader visualize and understand concepts in unexpected and memorable ways. Use conversational language that mimics advice from a witty and knowledgeable friend, making the tone informal and accessible. Utilize playful exaggeration for comedic effect, highlighting the absurdities or challenges of the topic in a light-hearted manner. Assign human attributes or behaviors to non-human elements (personification) to make the content more relatable and amusing. Craft an engaging introduction and conclusion with strong, humorous notes, setting a playful tone at the start and concluding with a punchline or insightful amusement at the end. Directly address the reader using 'you' to create a personal and engaging narrative, incorporating humorous asides and rhetorical questions to enhance engagement."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()


def buttonstyle_5():
    message = "Revise the previous article you have generated to change the writing style .  Do not greet the reader in the beginning of the article. The writing style has to include Informative Tone, Maintain an informative tone throughout the article, providing valuable insights and well-considered opinions. Casual Language, Use casual language and colloquial expressions to make the article engaging and relatable for readers. Historical References, Include historical references to provide context and depth to the topic. Comparative Analysis, Conduct comparative analysis, highlighting the unique features and differences between the subjects being discussed. Engagement with Readers, Actively engage with readers by inviting them to share their opinions and comments on the topic. Include a call-to-action for readers to participate in the discussion. Listicle Format, Structure the article as a listicle, with each item accompanied by a brief description and evaluation. Blend of Description and Critique, lend descriptive elements, such as features and themes, with critical analysis, evaluating the strengths and weaknesses of each item."

    #message = "Infuse consistent humor throughout your writing, including jokes, witty remarks, and amusing observations to keep it light and engaging. Employ imaginative analogies and metaphors to help the reader visualize and understand concepts in unexpected and memorable ways. Use conversational language that mimics advice from a witty and knowledgeable friend, making the tone informal and accessible. Utilize playful exaggeration for comedic effect, highlighting the absurdities or challenges of the topic in a light-hearted manner. Assign human attributes or behaviors to non-human elements (personification) to make the content more relatable and amusing. Craft an engaging introduction and conclusion with strong, humorous notes, setting a playful tone at the start and concluding with a punchline or insightful amusement at the end. Directly address the reader using 'you' to create a personal and engaging narrative, incorporating humorous asides and rhetorical questions to enhance engagement."
    st.session_state.article_generated.append(message)

    save_message(message)
    run_open_AI()

def buttonstyle_6():
    message = "Revise the previous article you have generated to change the writing style. Do not greet the reader in the beginning of the article. The new writing style has to include informal, conversational, and filled with humor and lots of sarcasm. to keep the reader entertained. Use some Pop Culture References, Employ some pop culture references to make the content relatable and engaging. Best to use gaming pop culture. Use of Profanity and Exaggerated Descriptions, Use profanity and exaggerated descriptions to convey opinions and experiences with intensity and flair. Casual and Colloquial Language, Use casual and colloquial language to engage the reader in a more personal and relatable way. Repetition, Exaggeration, and Comparison, Employ repetition, exaggeration, and comparison to make points more entertaining and memorable. Anecdotes and Comparisons, Incorporate anecdotes and comparisons to add humor and light-heartedness to the article."

    #message = "Infuse consistent humor throughout your writing, including jokes, witty remarks, and amusing observations to keep it light and engaging. Employ imaginative analogies and metaphors to help the reader visualize and understand concepts in unexpected and memorable ways. Use conversational language that mimics advice from a witty and knowledgeable friend, making the tone informal and accessible. Utilize playful exaggeration for comedic effect, highlighting the absurdities or challenges of the topic in a light-hearted manner. Assign human attributes or behaviors to non-human elements (personification) to make the content more relatable and amusing. Craft an engaging introduction and conclusion with strong, humorous notes, setting a playful tone at the start and concluding with a punchline or insightful amusement at the end. Directly address the reader using 'you' to create a personal and engaging narrative, incorporating humorous asides and rhetorical questions to enhance engagement."
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
    print(run.usage.total_tokens)
    
    df = conn.read(
    spreadsheet="https://docs.google.com/spreadsheets/d/1Y5oaJN_XDAy6iM7yVAKKqIofI1WICOmYKWCD3OVQ8E0/edit?usp=sharing"
    ,worksheet="Sheet3", usecols = [0,1,2,3])

    tokenloc = curtoken
    tokenadd = int(tokenloc) + int(run.usage.total_tokens)
    df.iloc[st.session_state.userLoc,3] = tokenadd
    st.session_state.tokenUsed = tokenadd
    df = conn.update(worksheet="Sheet3" ,data = df)
    st.cache_data.clear()  
    print(st.session_state.tokenUsed)    
    
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
            

def main_draft():
    
    


    message = "change the current article to html. make the conversion as just text HTML so i can copy paste it. i just want the <pr>, <br> and etc. i do not need the DOCTYPE info."
    with st.spinner('Sending Message'):
        save_message(message)

    with st.spinner('Generating Article'):
        run_open_AI()

    st.session_state.status_check = False

    draft()
    print("publish done")

    


if st.session_state.article_generated == []:
    st.session_state.status_check = True
else:
    st.session_state.status_check = False

  












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
            if st.button("listicle", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_1()

            if st.button("escapist 1", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_2()
        with col2:
            if st.button("expository", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_3()
            if st.button("blogging", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_4()
            if st.button("RPS article", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_5()
            if st.button("escapist 2", use_container_width = True, disabled = st.session_state.status_check):
                buttonstyle_6()




st.divider()

with st.container():
    col1, col2, col3 = st.columns([1,4,4])
    with col1:
        if st.button("Draft",disabled = st.session_state.status_check, use_container_width = True):
            main_draft()


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



if not st.session_state.validUser:
    with st.sidebar:
        st.write("Please Log in") 

else:
    with st.sidebar:
        st.write("User: " + str(st.session_state.user))
        st.write("Token used: " + str(int(st.session_state.tokenUsed)))
        money = (int(st.session_state.tokenUsed)/1000000) * 1.75
        st.write("Money used: " + str(money))
