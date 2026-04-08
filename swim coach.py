import anthropic
client = anthropic.Anthropic()
# The conversation history — starts empty
history = []
# User sends the first message
history.append({"role": "user", "content": "My name is Alex."})
# Send the history to Claude — just the first message so far
response = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=100,
messages=history
)
# Get Claude's response text
reply = response.content[0].text
print("Claude:", reply)
# Add Claude's response to the history
history.append({"role": "assistant", "content": reply})
# User sends a second message
history.append({"role": "user", "content": "What is my name?"})
# Send the FULL history — both messages — to Claude
response2 = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=100,
messages=history
)
print("Claude:", response2.content[0].text)