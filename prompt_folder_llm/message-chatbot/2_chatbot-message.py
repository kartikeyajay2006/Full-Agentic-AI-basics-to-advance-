from langchain_core.messages import HumanMessage , AIMessage , SystemMessage 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 

load_dotenv()

chat_history = [

]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["quit" , "exit"]:
        break
    llm = ChatGroq(model="llama-3.1-8b-instant")
    k= llm.invoke(chat_history)
    chat_history.append(AIMessage(content=k.content))
    print("AI: ",k.content)

print(chat_history)