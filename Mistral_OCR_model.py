import os
from mistralai import Mistral
import dotenv
dotenv.load_dotenv()
import base64

MISTRAL_API_KEY = os.getenv("MISTRAL_KEY")
client = Mistral(api_key = MISTRAL_API_KEY)

# uploaded_pdf = client.files.upload(
#     file={
#         "file_name": "uploaded_file.pdf",
#         "content": open("EMAI - After midsem.pdf", "rb"),
#     },
#     purpose="ocr"
# )  

# print("File uploaded successfully:", uploaded_pdf.id)
# file_url = client.files.get_signed_url(file_id = uploaded_pdf.id)

# ocr_response = client.ocr.process(
#     model = "mistral-ocr-latest",
#     document = {
#         "type" :"document_url",
#         "document_url" : file_url.url
#         },
#     include_image_base64 = True
# )

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": "https://educasia.org/wp-content/uploads/Atoms-and-Molecules-Students-book.pdf"
    },
    include_image_base64=True
)

def data_uri_to_bytes(data_uri):
  _, encoded = data_uri.split("," ,1)
  return base64.b64decode(encoded)

def export_image(images):
    parsed_image = data_uri_to_bytes(images.image_base64)
    with open(image.id, "wb") as image_file:
        image_file.write(parsed_image)

with open("digital_notes.md", "w", encoding="utf-8") as file:
  for page in ocr_response.pages:
    file.write(page.markdown)
    for image in page.images:
      export_image(image)

print("digital_notes.md created successfully with OCR results.")