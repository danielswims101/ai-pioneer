# gourmet_critic.py — AI food critic with personality
import anthropic
client = anthropic.Anthropic( )
# The system prompt defines who Claude will be for this whole program
critic_persona = (
"You are Sofia Chen, a renowned food critic who writes for the worlds top food magazines. "
"You have eaten at over 2,000 Michelin-starred restaurants across 40 countries. "
"You are honest, specific, and deeply knowledgeable about technique and ingredients. "
"You always give one thing to improve and one thing that was genuinely impressive. "
"You write in a confident, vivid style — never vague."
)
# Get the dish details
dish_name = input("Name of the dish you made or ate: ")
ingredients = input("Main ingredients used: ")
technique = input("How was it cooked (grilled, braised, raw, etc.): ")
your_verdict = input("How did you think it turned out (be honest): ")
# Build a detailed prompt — include all the specifics
prompt = (
f"I am telling you about a dish called {dish_name}. \n"
f"Main ingredients: {ingredients}. \n"
f"Cooking technique: {technique}. \n"
f"My own verdict: {your_verdict}. \n"
"Please give me your expert critique as Sofia Chen. "
"Be specific. Be honest. Include what worked and what to improve."
)
response = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=300,
system=(
    "You are Sofia Chen, a Michelin-starred Italian food critic with over 30 years experience. "
    "You are direct, passionate, and intolerant of mediocrity. "
    "You speak from deep technical knowledge of classical Italian cooking."
),
messages=[{"role": "user", "content": "I made poopy for the first time. I used a very fine poop piece and made it raw for you.The poop has been freshly farmed and slightly peppered and dried. How did I do?"}]
)
print("")
print("=== SOFIA CHEN — FOOD CRITIC ===")
print(response.content[0].text)