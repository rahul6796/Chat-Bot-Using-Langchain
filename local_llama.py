from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama


import os 
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# # langsmith for tracking:
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')





# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question : {question}")
    ]
)


# streamlit

st.title('Chat Bot')
input_txt = st.text_input('Search')


# ollama

llm = Ollama(model = "Gemma")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'question': input_txt }))

