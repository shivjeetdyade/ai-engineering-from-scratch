import os
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads .env into environment variables

client = anthropic.Anthropic()  # automatically picks up ANTHROPIC_API_KEY

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)

print(response.content[0].text)
