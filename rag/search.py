import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_collection("waste_items")


query = "Plastic Bottle"

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)

query_embedding = response.embeddings[0].values

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"][0])