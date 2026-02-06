from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

st.header("Research Tool")
user_input = st.text_input("Enter your prompt :=> ")

if st.button('summarize'):
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

        response = llm.invoke(user_input)
        st.write(response.content)