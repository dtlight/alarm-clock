import datetime
import time
from pygame import mixer

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
    print('Press "ctrl + c" to abort')
    current_day_value = -1
    travis_ci = True
    while True:
        today = datetime.datetime.now()
        day = today.strftime("%A")
        atUni = notAtUni(today)
        alarmTime = autoAlarm(day, atUni)
        #print alarm wake up time
        if current_day_value != datetime.datetime.today().weekday():
            current_day_value = datetime.datetime.today().weekday()
            print ("Next alarm is set for", alarmTime)
        mixer.init()
        mixer.music.load("alarm_noise.mp3")
        currentTime = today.strftime("%X")
        if currentTime[1:5] == alarmTime:
            mixer.music.play(5)
            time.sleep(5)
        if travis_ci:
            break
