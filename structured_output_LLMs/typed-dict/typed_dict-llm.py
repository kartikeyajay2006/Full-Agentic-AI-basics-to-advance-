from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from typing import TypedDict
from typing_extensions import Annotated

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# Schema - for data (creating structured data format)
class Review(TypedDict):
    key_themes: Annotated[list[str], "Key themes mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Overall sentiment: positive, negative, or neutral"]

structured_model = llm.with_structured_output(Review)

# Example usage
response = structured_model.invoke(
    "The phone has a great camera and battery life, but the performance is slow."
)

print(response)