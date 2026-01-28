import os
from persona import PROMPT
from posts import POST_1, POST_2
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    messages=[
        {
            "role": "user",
            "content": PROMPT
        }
    ],
    temperature=0.8,
)

clean_text = completion.choices[0].message.content

# Write to posts.py
if POST_1 == "":
    with open('posts.py', 'w', encoding='utf-8') as f:
        f.write(f'POST_1 = """{clean_text}"""')
else:
    with open('posts.py', 'w', encoding='utf-8') as f:
        f.write(f'POST_2 = """{clean_text}"""')

print(clean_text)