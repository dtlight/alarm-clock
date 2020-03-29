'''
Unit tests for alarm_clock.py, dayOfTheWeekNoUni checks the correct time is returned for a day with no uni.
Likewise, dayOfTheWeekUni checks the correct time is returned for a day with uni.
'''
import unittest
import alarm_clock

class AutoAlarmTests(unittest.TestCase):

    def test_ThursdayNoUni(self):
        result = alarm_clock.autoAlarm("Thursday", True)
        self.assertEqual('9:00', result)

    def test_MondayUni(self):
        result = alarm_clock.autoAlarm("Monday", False)
        self.assertEqual('6:00', result)

    def test_TuesdayUni(self):
        result = alarm_clock.autoAlarm("Tuesday", False)
        self.assertEqual('6:00', result)

    def test_MondayNoUni(self):
        result = alarm_clock.autoAlarm("Monday", True)
        self.assertEqual('9:00', result)

    def test_ThursdayUni(self):
        result = alarm_clock.autoAlarm("Thursday", False)
        self.assertEqual('7:30', result)

    def test_FridayUni(self):
        result = alarm_clock.autoAlarm("Friday", False)
        self.assertEqual('6:00', result)

    def test_SaturdayNoUni(self):
        result = alarm_clock.autoAlarm("Saturday", True)
        self.assertEqual('9:00', result)

    def test_SaturdayUni(self):
        result = alarm_clock.autoAlarm("Saturday", False)
        self.assertEqual('9:00', result)

    def test_SundayUni(self):
        result = alarm_clock.autoAlarm("Sunday", False)
        self.assertEqual('9:00', result)

if __name__ == '__main__':
    unittest.main()