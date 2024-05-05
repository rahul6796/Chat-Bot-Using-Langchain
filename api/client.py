
import requests
import streamlit as st


# calling api

def get_api_response(input_text):
    response = requests.post("http://localhost:8002/essay_ollama_model/invoke",
                             json= {'input': {'topic': input_text}})
    
    return response.json()['output']

# calling streamlit
st.title('Chat-Bot Using Gemma Model !')
input_text = st.text_input('Write an easy essay')


if input_text:
    st.write(get_api_response(input_text=input_text))
    


