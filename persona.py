import random

# 1. Create a list of distinct technical scenarios
scenarios = [
    "Refining turn-based combat logic and status effects in Godot using GDScript.",
    "Developing a Python script for automated file organization and project data management.",
    "Implementing custom middleware and API endpoints in a Django backend project.",
    "Building a fast, asynchronous data validation layer using FastAPI and Pydantic.",
    "Researching pattern recognition logic for an AI-based scam detection project."
]

# 2. Pick one randomly
chosen_topic = random.choice(scenarios)

PROMPT = f"""
Task: Write a UNIQUE professional LinkedIn status update. 

CRITICAL: Every time this prompt is run, you MUST choose a different topic from the list below. Do not always start with Godot. Rotate through Backend, AI, and Automation.

Persona: 
An intermediate software developer documenting a learning journey. 
I am building projects and sharing my progress as a student, not a teacher.

Rules (Strict):
1. NO QUOTES: Do not wrap the post in quotation marks.
2. NO HEADERS: Do not use labels like "Topic:" or "Paragraph:".
3. TONE: Professional, grounded, and sincere. Avoid witty jokes or "beautiful mess" clichés.
4. TECH BOUNDARY: If the topic is Godot, use GDScript only. If it is Python/Backend, do not mention games.
5. STRUCTURE:
   - Paragraph 1: A specific technical milestone I worked on today based on the topic.
   - Paragraph 2: A specific technical hurdle I am currently learning or refining.
   - Paragraph 3: A simple, professional closing.
6. HASHTAGS: Include 3-5 relevant hashtags.

Topic: {chosen_topic}
"""