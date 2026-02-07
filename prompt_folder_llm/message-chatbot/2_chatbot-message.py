from langchain_groq import ChatGroq 
from langchain_core.messages import SystemMessage , HumanMessage, AIMessage 
from dotenv import load_dotenv 
load_dotenv()

chat_history=[
    SystemMessage(content="You are a AI assistamt that helps us to answer the queries of users.")

]

while True:
    user_input  = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input in ["exit","quit"]:
        break
    llm = ChatGroq(model="llama-3.1-8b-instant")
    res = llm.invoke(chat_history)
    chat_history.append(AIMessage(content = res.content))
    print("AI: ",res.content)