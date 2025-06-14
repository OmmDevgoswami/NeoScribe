import time
from mem0 import MemoryClient
from mem0.client.main import APIError
import os
import dotenv


dotenv.load_dotenv()

MEM0_API_KEY = os.getenv("MEM0_KEY")
AGNO_OUTPUT_PATH = "quick_notes.md"

client = MemoryClient(api_key=MEM0_API_KEY)
user_id = "neoscribe"

def parse_agno_output(text):
    sections = {}
    current_key = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("## "):
            current_key = line[3:].strip()
            sections[current_key] = ""
        elif current_key:
            sections[current_key] += line + "\n"
    return sections

def load_markdown_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def format_for_mem0(parsed):
    messages = []
    for qna in parsed.get("Flashcards", "").split("\n\n"):
        if qna.startswith("Q:") and "A:" in qna:
            q, a = qna.split("\nA:", 1)
            messages.append({"role": "user", "content": q.strip()})
            messages.append({"role": "assistant", "content": "A:" + a.strip()})
            
    quiz_section = parsed.get("Quiz MCQs", "").strip()
    if quiz_section:
        messages.append({"role": "user", "content": "Add these MCQ-style quiz questions:"})
        messages.append({"role": "assistant", "content": quiz_section})

    summary = parsed.get("Note Summary", "").strip()
    if summary:
        messages.append({"role": "user", "content": "Summarize the key concepts in a short note."})
        messages.append({"role": "assistant", "content": summary})

    return messages

def chunked(iterable, size):
    """Yield successive chunks from iterable."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

def push_to_mem0(messages, user_id, batch_size=5):
    client = MemoryClient(api_key=os.getenv("MEM0_KEY"))
    for i, batch in enumerate(chunked(messages, batch_size)):
        try:
            print(f"📤 Uploading batch {i + 1}/{(len(messages) + batch_size - 1) // batch_size}...")
            client.add(batch, user_id=user_id)
            time.sleep(1)  # slight delay to avoid rate limiting
        except APIError as e:
            print(f"❌ Error uploading batch {i + 1}: {e}")
    client.add(messages, user_id=user_id)
    print(f"✅ Successfully added {len(messages)//2} knowledge units to Mem0 for user '{user_id}'.")

def run_pipeline():
    content = load_markdown_content(AGNO_OUTPUT_PATH)
    parsed = parse_agno_output(content)
    messages = format_for_mem0(parsed)
    push_to_mem0(messages, user_id)
    
if __name__ == "__main__":
    run_pipeline()
