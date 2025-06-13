from spellchecker import SpellChecker
import re

spell = SpellChecker()

def correct_spelling(text):
    words = re.findall(r'\b\w+\b', text)
    corrected_text = text
    for word in words:
        if word.lower() in spell:
            continue
        correction = spell.correction(word)
        if correction and correction != word:
            corrected_text = re.sub(r'\b' + re.escape(word) + r'\b', correction, corrected_text)
    return corrected_text

# Example usage
with open("output.md", "r", encoding="utf-8") as f:
    raw_markdown = f.read()

cleaned_markdown = correct_spelling(raw_markdown)

with open("output_cleaned.md", "w", encoding="utf-8") as f:
    f.write(cleaned_markdown)
