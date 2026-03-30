# fishing_game.py
# =====================================================
# Program: fishing_game.py
# What it does: A fishing simulator using while loops
# =====================================================
# import random gives us access to random number tools
import random
# This is a list of possible fish to catch
# We'll pick from this list randomly
fish_pool = [
"Bass (2 lbs)",
"Catfish (4 lbs)",
"Trout (1 lb)",
"Pike (6 lbs)",
"Walleye (3 lbs)",
"Nothing — got away!",
"Nothing — no bite.",
"Old boot (disgusting)",
]
# Counters — we'll track how many fish and casts
fish_count = 0
cast_count = 0
print("=== FISHING SIMULATOR ===")
print("Press Enter to cast your line. Type q to go home.")
print("")
# The while loop runs as long as the condition is True
# We use True here to mean 'run forever until we say stop'
keep_fishing = True
while keep_fishing:
# Ask if they want to cast or quit
action = input("Cast your line? (Enter=yes, q=quit): ")
if action.lower() == "q":
# They want to quit — set keep_fishing to False
# This causes the while loop to stop
keep_fishing = False
else:
# They want to cast
cast_count = cast_count + 1
print("Casting...")
# random.choice() picks one random item from the list
result = random.choice(fish_pool)
print("Result:", result)
# Check if they caught something real (not nothing/boot)
if "Nothing" not in result and "boot" not in result:
fish_count = fish_count + 1
print("Nice catch! Total fish:", fish_count)
print("")