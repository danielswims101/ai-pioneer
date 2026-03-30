event = input( "What event are you checking?: ")
time_text = input("Enter time in seconds: ")
time = float(time_text)

if time < 52:
    level = "ELITE  - National championship territory"
    advice = "You are swimming at a very high level. Keep going."
elif time < 57:
    level = "EXCELLENT - High school varsity level"
    advice = "Strong time. Consistency will bring you to elite"
elif time < 62:
    level = "DEVELOPING - Solid dristrict level performance"
    advice = "Good foundation. Focus on turns and starts"
elif time < 68:
    level = "DEVELOPING - Building toward competetive"
    advice = "Every practice is a step forward track your improvemnets"
else:
    level = "EARLY STAGE - The work startsx now"
    advice = "Every champion swimmer had a day one time. This is yours"
print("")
print("=== SWIM TIME ANALYSIS===")
print("Event:", event)
print("Time:", time, "seconds")
print("Level:", level)
print("Coach note:", advice)