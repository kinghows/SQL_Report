# SQL_Report
Export SQL to HTML report,export SQL to txt/csv/xls file.

MySQL need install mysql-python:

pip install mysql-python

Oracle  need install cx_Oracle

pip install cx_Oracle

Save as xlsx need install pandas,openpyxl:

easy_install openpyxl

pip install pandas

Test in Python-2.7

Edit  connect info in dbset.ini [database] part.

Edit you SQL  info in dbset.ini [[report]] part.

example:

report_count = n

#---m---------------------------------

titlem = ***

querym = ***

stylem =***

n must <=m

example:

![txt example](https://github.com/kinghows/SQL_Report/blob/master/txt.jpg)
![html example](https://github.com/kinghows/SQL_Report/blob/master/html.jpg)

execute:

python sql_report.py >my_report.html

python sql_report.py -p dbset.ini >my_report.html

python sql_report.py -p dbset.ini -s html >my_report.html

python sql_report.py -p dbset.ini -s txt

python sql_report.py -p dbset.ini -s csv

python sql_report.py -p dbset.ini -s xls

send email:

python SendEmail.py -p emailset.ini -f my_report1.html,my_report2.html

use crontab regularly perform sql_report.sh,auto generate  report,and send email.

If your mysql report results are in other languages, modify the cursor.execute('SET NAMES GBK') as the appropriate encoding format.

Enjoy it! 
