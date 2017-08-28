#!/bin/sh
report_base=/services/script
datetime=`date +%Y-%m-%d_%H-%M`
python $report_base/sql_report.py -p $report_base/dbset101.ini  -s html>$report_base/my_report101_$datetime.html
python $report_base/sql_report.py -p $report_base/dbset102.ini  -s html>$report_base/my_report102_$datetime.html
python SendEmail.py -p emailset101.ini -f $report_base/my_report101_$datetime.html,$report_base/my_report102_$datetime.html