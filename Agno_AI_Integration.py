from agno.agent import Agent, RunResponse
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.google import Gemini
import os
import dotenv

dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")

model = Gemini(
    id="gemini-2.0-flash-exp",
    name="Buddy",
    api_key=GEMINI_API_KEY,
    temperature=0.7,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

AGNO_PROMPT = """
You are Agno AI, the core semantic brain behind NeoScribe — a smart assistant that transforms messy handwritten academic notes into clean, structured digital learning content.

Your task is to:
1. Analyze the input academic content and output the following:
   - Main Topic
   - Clear Subtopics
   - One-line Summary per Subtopic
   - Prerequisite Concepts
   - Learning Difficulty (Beginner / Intermediate / Advanced)
   - Insights or Warnings (if applicable)
2. If the content contains image references or links:
   - Attempt to preserve them in markdown using `![Alt Text](path_or_description)` syntax.
   - If unable to embed, just list them as: 
     **Image X:** [brief description]
   - Append all image descriptions at the end under `## Referenced Images`.

3. Format everything in markdown for readability and digital publishing.
4. Use concise, clear academic language.

In addition, you should:
- Generate a few flashcards with Q&A format.
- Include 3 - 4 possible quiz MCQs from the content.
- Provide a short note summary for memorization purposes.

Flash card format:
Q: What is ... ?
A: The Answer is ...

Quiz format:
Q: Which of the following is true about ...?
Option: A) Option 1 
B) Option 2 
C) Option 3 D) Option 4
A: The correct answer is B) Option 2.

Use the DuckDuckGo tool to search for any additional information needed to clarify concepts or provide context.
Mkae sure to include all relevant information in your response.

Everything should be markdown-friendly and easy to parse by an external memory engine.
"""

agent = Agent(
    model=model,
    description=AGNO_PROMPT,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

with open("digital_notes.md", "r", encoding="utf-8", errors="replace") as f:
    markdown_content = f.read()

agent.print_response(
    "Analyze the following academic content and provide a structured summary:\n\n" + markdown_content,
    stream=True,
)

response: RunResponse = agent.run(
    "Analyze the following academic content and provide a structured summary:\n\n" + markdown_content,
    stream=False
)

agno_output = response.content

with open("quick_notes.md", "w", encoding="utf-8") as out:
    out.write(agno_output)
