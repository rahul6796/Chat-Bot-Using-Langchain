
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama


app = FastAPI(
    title='Langchai Server',
    version='0.0.1',
    description='A simple llm api server'
)


llm = Ollama(model = "gemma:2b")

prompt  = ChatPromptTemplate.from_template(
    "write me essay on this given topic {topic} with 100 words."
)


add_routes(
    app,
    prompt|llm,
    path="/essay_ollama_model")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)



