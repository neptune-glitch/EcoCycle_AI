import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

print("API Key:", os.getenv("GEMINI_API_KEY"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def identify(image_path: str) -> str:
    print("Opening image:", image_path)

    image = Image.open(image_path)

    print("Sending request to Gemini...")

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

    print("Gemini Response:", response.text)

    return response.text.strip()