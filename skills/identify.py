import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def identify(image_path: str) -> str:
    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            image,
            """
            Identify this waste item.

            Return ONLY the item name.

            Example:
            Plastic Bottle
            """
        ]
    )

    return response.text.strip()