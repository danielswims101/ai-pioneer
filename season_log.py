# season_log.py
# =====================================================
# Program: season_log.py
# What it does: Logs a swim season and analyzes it
# =====================================================
print("=== SWIM SEASON ANALYZER ===")
print("")
event = input("What event are we logging? (e.g., 100 freestyle): ")
season = input("What season? (e.g., Winter 2026): ")
num_text = input("How many meets did you race in? ")
num_meets = int(num_text)
# Create an empty list to hold the times
race_times = []
print("")
print("Enter your official time from each meet (in seconds).")
print("Go in order from your first meet to your most recent.")
print("")
for meet_number in range(1, num_meets + 1):
prompt = "Meet " + str(meet_number) + " time: "
time_input = input(prompt)
time = float(time_input)
race_times.append(time)
# Analysis time
print("")
print("==============================")
print(" SEASON ANALYSIS")
print("==============================")
print("Swimmer event:", event)
print("Season:", season)
print("Meets raced:", num_meets)
print("")
print("Season best:", min(race_times), "sec")
print("Season slowest:", max(race_times), "sec")
print("Season average:", round(sum(race_times) / len(race_times), 2), "sec")
# Calculate improvement: first meet vs last meet
first_time = race_times[0]
last_time = race_times[-1]
improvement = round(first_time - last_time, 2)
print("")
if improvement > 0:
print("Season improvement:", improvement, "seconds faster!")
elif improvement < 0:
print("Slight regression:", abs(improvement), "sec slower than start.")
print("This happens. Look at your best vs the start instead.")
else:
print("Same time start to finish. Consistency is a foundation.")