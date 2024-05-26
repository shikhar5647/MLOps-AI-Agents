import streamlit as st
import langchain
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
st.set_page_config(page_title="Chatbot developed by Shikhar Dave")
st.header("Hey , let's Chat now buddy")


from dotenv import load_dotenv
load_dotenv()
import os

# Directly set the OpenAI API key
openai_api_key = "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"

# Initialize the ChatOpenAI class with the API key
chat = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a helpful AI Assistant")
    ]

def get_openai_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)