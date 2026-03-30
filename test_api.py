import anthropic
client = anthropic.Anthropic()
 
response = client.messages.create(
    model="claude-haiku-4-5-2025001",
    max_tokens=80,
    messages=[
        {"role": "user",
         "content": "Say hello and one cool fact about competetive swimming."}
    ]
)