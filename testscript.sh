#/usr/bin/env/sh
set -e

for script in test_alarm_clock.py alarm_clock.py
do
  python3 $script
done
