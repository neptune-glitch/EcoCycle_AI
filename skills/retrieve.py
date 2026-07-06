import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="chroma_db")

try:
    collection = chroma_client.get_collection("waste_items")
except chromadb.errors.NotFoundError:
    import build_db
    collection = chroma_client.get_collection("waste_items")


def retrieve(item: str) -> str:
    """
    Retrieve recycling knowledge for a waste item.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=item
    )

    embedding = response.embeddings[0].values

    results = collection.query(
        query_embeddings=[embedding],
        n_results=1
    )

    if results["documents"] and results["documents"][0]:
        return results["documents"][0][0]

    return "No recycling information found."