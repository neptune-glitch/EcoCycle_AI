import pandas as pd
import chromadb
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection("waste_items")

df = pd.read_csv("data/waste_knowledge.csv")
for index, row in df.iterrows():

    text = f"""
    Item: {row['Item']}
    Material: {row['Material']}
    Recyclable: {row['Recyclable']}
    Reuse Ideas: {row['Reuse Ideas']}
    Compostable: {row['Compostable']}
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    embedding = response.embeddings[0].values

    collection.add(
        ids=[str(index)],
        embeddings=[embedding],
        documents=[text]
    )

print("Knowledge Base Embedded Successfully!")