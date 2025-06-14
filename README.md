# NeoScribe
This is a contribution under My Summer Internship with Build Fast with AI

## Inspiration
Summarized notes are the true saviour during those last night study session and with this motivation I build NeoScribe to make summarized notes from pdfs and images with Key Takeaways, Flashcards and Quiz for qucik revision and preparation.

## What it does
It takes PDFs, Images and convert them into well structured Markdown for clean reading and exploration of the notes. 
- PDF to Markdown formart
- Images to Text in JSON format
- Summarized Final Notes and Quick revision topic wise

## Tech Stack Used:
---
- Mistral AI : For OCR conversion
- Agno AI + Gemini-2.0-flash: For Summarized notes + Flash Card/Quiz/Summary Generation
- Memo0 for storage and practice 
---

## All Import files : requiments.txt
``` pip install -r requiments.txt ```
- mistralai>=0.1.2
- mem0>=0.0.7
- agno>=0.1.6
- python-dotenv>=1.0.0
- transformers>=4.40.0
- duckduckgo-search>=0.9

## INSTALLATION:
### To run NeoScribe locally, follow these steps:
1. On the GitHub page for this repository, click on the button "Fork."
2. Clone your forked repository to your computer by typing the following command in the Terminal: 
``` git clone https://github.com/<your-github-username>/NeoScribe.git ```
4. Navigate into the cloned repository by typing the following command in the Terminal:
``` cd /NeoScribe ```
5. Run the "**Mistral_OCR_model.py**" to convert pdfs into Markdown fromat.
6. Incase of image convertion, Run "**image-to-text.py**" and pass the image you wish to have json format of.
7. After conversion, pass the Markdown file Through Agno-AI Model.
8. Run the "**Agno_AI_Integration.py**" to summarize the markdown and produce a refined markdown with Quizes, Flash Cards and Summaries for easier learning.
9. Run the "**Mem0_pipline.py**" to store the refined markdown data into the Vector database.
10. Run the "**View_the_Content.py**" to interact with the Mem0 database and access datatopic wise.
###                                        or
1. Use the google collab file: https://colab.research.google.com/drive/1_RLwvQjfVFRMUmI_ad-l7QXxe9PyLld9?usp=sharing to run and test directly the outcomes !!

## What's next for NeoScribe
1. Improvement in ther overall Model - Agno AI + Mem0
2. A cleaner UI + Dashbaord for accessing all data in a better way
3. Drag-n-Drop Feature
4. Overall alot of improvements

