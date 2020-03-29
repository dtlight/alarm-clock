
def autoAlarm(day, noUni):
	weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
	weekends = ["Saturday","Sunday"]
	if day in weekends:
		return "9:00"
	elif day in weekdays and noUni:
		return "9:00"
	else:
		return "7:45" if day == "Wednesday" or day == "Thursday" else "6:00"
