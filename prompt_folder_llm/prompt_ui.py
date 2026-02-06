from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()

st.markdown("<P style='text-align: center; color: red; font-size: 30px;'>WELCOME TO THE PROMPT UI</P>", unsafe_allow_html=True)
st.header("ENTER YOUR PROMPT")

k =st.text_input("Enter your prompt here:=> ")

if st.button("submit"):
    if (k.strip()==""):
        st.warning("Please enter a valid prompt")
    else:
        llm =ChatGoogleGenerativeAI(model="gemini-2.5-flash") 
        res =llm.invoke(k)
        st.write(res.content)