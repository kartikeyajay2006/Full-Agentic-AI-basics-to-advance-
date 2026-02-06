from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

ques=input("enter your question:-- ")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

k = llm.invoke(ques)
print(k.content)
