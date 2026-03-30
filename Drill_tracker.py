print("===SWIM DRILL TRACKER===")
print("")

reps_text = input("How many reps in today's drill set?")
reps = int(reps_text)

drill = input("What drill are you doing?")

times = []

print("")
print("Enter your time for each rep in seconds.")
print("")

for rep_number in range(1,reps + 1):
    prompt = "Rep " + str(rep_number) + "time (seconds): "
    time_text = input(prompt)
    time = float(time_text)
    times.append(time)

print("")
print("==Drill Set Results==")
print("Drill:", drill)
print("Reps completed:", reps)

print("Best rep:", min(times), "seconds")
print("Slowest rep:", max(times), "seconds")
print("Average time:", round(sum(times) / len(times), 2), "seconds")
print("")
print("All reps:")
for i in range(len(times)):
    print(" Rep", i +1, ":", times[i], "seconds")