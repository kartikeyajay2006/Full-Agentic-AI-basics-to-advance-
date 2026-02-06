from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_history=[]

while True:
    user_input =input("User: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        break
    K = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    res =K.invoke(chat_history)
    chat_history.append(res.content)
    print("AI: ",res.content)   