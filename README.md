# Automated Alarm Clock
[![Build Status](https://travis-ci.com/dave-light/alarm-clock.svg?token=8VzQcFZGdx7xQoVYeEZv&branch=master)](https://travis-ci.com/dave-light/alarm-clock)

An automated alarm clock that adjusts depending on the day of the week and whether I am at university (term time) or on not

----------
* ***If it's a standard term day***...
  * I need to wake up at 6:00 on Mondays, Tuesdays and Fridays
  * and at 7:45 on Wednesdays and Thursdays
* ***If there is no uni on a weekday*** (it's Easter, Christmas or summer holidays),
  * then I can wake up at 9:00

* ***If it's a weekend***
  * I always wake up at 9:00am on the weekends (regardless of the day or whether it's in or out of term time)

**Inputs:**
----------
* **autoAlarm()** receives two inputs (string and boolean): *day* and *noUni*
  * **day** is a string ("Monday", "Tuesday", "Wednesday"...)
  * **noUni** is a boolean
    * True = if it's a vacation, holiday, or summer
    * False = if it's a standard term day, when lectures take place

**Output:**
------------
autoAlarm() returns one output (a string): time (e.g. "6:00")

**Examples:**
Inputs => output
--------------------------------
* Wednesday True => 9:00
* Monday False => 6:00
* Monday True => 9:00
* Wednesday False => 7:45
* Saturday True => 9:00
* Sunday False => 9:00

**Usage:**
--------------------------------
set travis_ci to False.

run:
``` python3 alarm_clock.py```

type "ctrl + C" to abort