import requests
from requests.auth import HTTPBasicAuth
import streamlit as st

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

api_url = "https://www.zenosyne.info/wp-json/wp/v2/posts"

username = "roboaut"
password = "HOpI 1u2n j4CP ZTt2 uRwx amFb"
article_status = "publish"
article = """
<h4>Bristla: The Thorny Guardian of the Forests</h4>
<p>Bristla, with its greenish humanoid form adorned with thorns and a ruddy bramble coiffure, stands out as a captivating Grass element Companion in Palworld. Renowned for its venomous thorns and amiable kinship with Cinnamoth, this Companion exudes a unique allure. In the untamed wilderness, Bristla may be sighted roaming near clusters of Cinnamoth, revealing its placid nature unless provoked. Its active talents, from Wind Cutter to Solar Blast, accentuate its formidable prowess in engagements.</p>

<!-- Include other article content here -->

<p>In summation, Grass companions in Palworld present a diverse array of capabilities, temperaments, and forms, enriching the gaming experience and narrative intricacy of this fantastical realm. Whether it be the prickly protector Bristla, the graceful courier Wumpo Botan, the fragrant associate Broncherry, or the jubilant floater Flopie, each Grass Companion contributes a unique essence to the magical cosmos of Palworld. Embrace the adventures that beckon as you forge alliances and devise strategies with these extraordinary Grass type Companions in your odyssey through Palworld.</p>
"""

post_data = {
    "title": "test title",
    "content": article,
    "status": article_status,


}

def publish():
    print("run function")
    response = requests.post( 
    api_url, 
    auth=HTTPBasicAuth(username, password), 
    json=post_data, 
) 
    return print(response)
 






if st.button("Publish test"):
    print("publish button pushed")
    publish()
    