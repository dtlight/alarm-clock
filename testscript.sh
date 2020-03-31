#/usr/bin/env/sh
set -e
scripts="test_alarm_clock.py alarm_clock.py"

for script in $scripts
do
  python3 script
done
