from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding =GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")


documents = [
    "Virat kohli is the indian batsman who is famour for his aggression and best batting skills",
    "Ms dhoni is a indian wicket kipper which is famour for his leadership and calm under pressure . A only captain with all icc trophies",
    "Joe root an english batsman famous for his skills and long batting - current best test batsman",
    "Jasprit Bhumrah , Mitchell Starch , Jofra Archer are the best fast bowlers of current time",
    "And at last i am kartikeya yadav the baap pf all the og name - undefeatedera came for him . The best in Artificial-Intelligence and Machine-learning"
]

query = "who is in artificial intelligence and machine learning ?"

doc_embeddings=embedding.embed_documents(documents)
querry_embeddings = embedding.embed_query(query)

scores = cosine_similarity([querry_embeddings] ,doc_embeddings)[0]
index , score = sorted(list(enumerate(scores)) , key=lambda x:x[1])[-1]
print(query)
print(documents[index])
