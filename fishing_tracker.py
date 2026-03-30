# fishing_tracker_app.py
# =====================================================
# Program: fishing_tracker_app.py
# The most complete program you've built so far.
# Uses: variables, if/else, loops, lists, file I/O
# =====================================================
import random
# The filename where we save all catches
SAVE_FILE = "my_catches.txt"
# ---- FUNCTION 1: Save a catch to file ----
# A function is a reusable block of code with a name.
# We haven't learned functions deeply yet, but copy this
# and it will work. We'll fully cover functions next week.
def save_catch(species, weight, location):
with open(SAVE_FILE, "a") as f:
line = species + "," + str(weight) + "," + location + "\n"
f.write(line)
# ---- FUNCTION 2: Load all catches from file ----
def load_catches():
catches = []
try:
with open(SAVE_FILE, "r") as f:
for line in f:
line = line.strip()
if line:
parts = line.split(",")
if len(parts) == 3:
catches.append({
"species": parts[0],
"weight": float(parts[1]),
"location": parts[2]
})
except FileNotFoundError:
pass # If no file exists yet, just return empty list
return catches
# ---- FUNCTION 3: Display all catches ----
def show_catches(catches):
if len(catches) == 0:
print("No catches logged yet. Get fishing!")
return
print("")
print("=== YOUR CATCH HISTORY ===")
for i in range(len(catches)):
c = catches[i]
print(str(i+1) + ".", c["species"], "|",
c["weight"], "lbs |", c["location"])
print("Total catches:", len(catches))
# Find the biggest fish
biggest = max(catches, key=lambda x: x["weight"])
print("Personal best:", biggest["species"],