import datetime

def autoAlarm(day, noUni):
	weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
	weekends = ["Saturday","Sunday"]
	if day in weekends:
		return "9:00"
	elif day in weekdays and noUni:
		return "9:00"
	else:
		return "7:45" if day == "Wednesday" or day == "Thursday" else "6:00"

def notAtUni(date):
    '''
    Check whether or not I am at university. 
    '''
    termMonths = ["Jan", "Feb", "Mar", "May", "Sep", "Oct", "Nov"]
    if date.strftime("%b") in termMonths:
        return False
    else:
        return True

if __name__ == '__main__':
    today = datetime.datetime.now()
    day = today.strftime("%A")
    atUni = notAtUni(today)
    alarmTime = autoAlarm(day, atUni)
    print ("Alarm is set for", alarmTime)