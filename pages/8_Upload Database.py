import streamlit as st
import openai
import requests
import json

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Streamlit UI
st.title("Upload File to OpenAI Database")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "json", "pdf"])

if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size, "bytes")
    
    # Read the file content
    file_content = uploaded_file.read()
    
    # Convert file content to a format suitable for the OpenAI API (e.g., base64, binary)
    # Depending on the API requirements, you may need to adjust this part
    files = {
        'file': (uploaded_file.name, file_content)
    }

    # Replace with the actual URL and parameters for your OpenAI API endpoint
    url = "https://api.openai.com/v1/files"

    # Make the API request
    response = requests.post(url, headers={"Authorization": f"Bearer {openai.api_key}"}, files=files)
    
    if response.status_code == 200:
        st.success("File uploaded successfully!")
        st.write(response.json())
    else:
        st.error("Failed to upload the file.")
        st.write(response.json())
