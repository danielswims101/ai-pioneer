import anthropic
client = anthropic.Anthropic()
# CALL A — vague prompt, no system context
response_a = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=150,
messages=[{"role": "user", "content": "Is pasta good?"}]
)
# CALL B — system prompt + detailed user prompt
response_b = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=150,
system=(
"You are Marco, a Michelin-starred Italian chef with 30 years experience. "
"You are direct, passionate, and intolerant of mediocrity. "
"You speak from deep technical knowledge of classical Italian cooking."
),
messages=[{"role": "user", "content": "I made spaghetti aglio e olio for the first time. I used regular spaghetti, pre-minced garlic from a jar, and dried parsley. The pasta water was lightly salted. How did I do?"}]
)
print("VAGUE ANSWER:", response_a.content[0].text)
print("")
print("EXPERT ANSWER:", response_b.content[0].text)