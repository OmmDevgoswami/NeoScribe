import base64
from pathlib import Path
import json
import os
from mistralai import Mistral
import dotenv

dotenv.load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_KEY")
client = Mistral(api_key=MISTRAL_API_KEY)

IMAGE_PATH = "note2.jpg"
image_file = Path(IMAGE_PATH)

if not image_file.is_file():
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

encoded = base64.b64encode(image_file.read_bytes()).decode()
base64_data_url = f"data:image/jpeg;base64,{encoded}"

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "image_url",
        "image_url": base64_data_url
    }
)

image_ocr_markdown = ocr_response.pages[0].markdown

chat_response = client.chat.complete(
    model="open-mistral-7b",  
    messages=[
        {
            "role": "user",
            "content": f"""This is image's OCR in markdown:
<BEGIN_IMAGE_OCR>
{image_ocr_markdown}
<END_IMAGE_OCR>.
Convert this into a sensible structured JSON response. The output should be strictly JSON with no extra commentary."""
        },
    ],
    response_format={"type": "json_object"},
    temperature=0
)

response_dict = json.loads(chat_response.choices[0].message.content)
json_string = json.dumps(response_dict, indent=4)

print("✅ Structured JSON Response:\n")
print(json_string)
