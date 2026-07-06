import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def advise(item, knowledge):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are EcoCycle AI.

Detected Item:
{item}

Knowledge Base:
{knowledge}

Using ONLY the knowledge above, provide:

1. Material
2. Recyclable?
3. Reuse Ideas
4. Compostable?
5. One eco-friendly tip.

Format the response nicely.
"""
    )

    return response.text