import os
import pandas as pd
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection("waste_items")

# Only build if collection is empty
if collection.count() == 0:

    df = pd.read_csv("data/waste_knowledge.csv")

    for i, row in df.iterrows():

        document = f"""
Item: {row['Item']}
Material: {row['Material']}
Recyclable: {row['Recyclable']}
Reuse Ideas: {row['Reuse Ideas']}
Compostable: {row['Compostable']}
"""

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=document
        )

        embedding = response.embeddings[0].values

        collection.add(
            ids=[str(i)],
            documents=[document],
            embeddings=[embedding]
        )

    print("Knowledge Base Created Successfully!")