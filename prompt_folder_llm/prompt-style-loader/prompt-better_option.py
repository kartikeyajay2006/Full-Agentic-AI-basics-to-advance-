import streamlit as st 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

st.markdown("<P style='text-align: center; color: red; font-size: 30px;'>WELCOME TO THE PROMPT UI</P>", unsafe_allow_html=True)

st.header("ENTER YOUR PROMPT")
k = st.text_input("Enter your prompt here:=> ")

with open("prompt_template.json","r") as f :
    template = f.read()

style = st.selectbox("Select Your Explanation Style", ["concise", "detailed", "step-by-step"])
length = st.selectbox("Select Your Response Length", ["short", "medium", "long"])

if st.button("submit"):
    if (k.strip()==""):
        st.warning("Please enter a valid prompt")
    else:
        final_prompt = template.format(style=style, length=length, user_prompt=k)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash") 
        res = llm.invoke(final_prompt)
        st.write(res.content)
