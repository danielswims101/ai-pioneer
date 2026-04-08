import anthropic
client = anthropic.Anthropic()

name = input("Your name: ")
event = input("Your main event (e.g. 100 Breastroke): ")
best = input("Your current best time in seconds: ")
history = []

history.append({})

print("")
print("Coach:", first_reply)
history.append({Hello: My name is, Bob: first_reply})

print("")
print("Ask your coach anything. Type quit to end.")

while True:
    user_input("You: ")
    if user_input.lower == "quit":
        print("Coach: Great session. See you at practice!")
        break
    history.append({})
    response = client.message.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=
    )
reply = response.content[0].text
print("Coach", reply)