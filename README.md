# SQL_Report
Export SQL to HTML report,export SQL to txt file.

MySQL need install mysql-python:

pip install mysql-python

Oracle  need install cx_Oracle

pip install cx_Oracle

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

execute:

python sql_report.py >my_report.html

python sql_report.py -p dbset.ini >my_report.html

python sql_report.py -p dbset.ini -s html >my_report.html

python sql_report.py -p dbset.ini -s txt

use crontab regularly perform sql_report.sh

If your report results are in other languages, modify the cursor.execute('SET NAMES GBK') as the appropriate encoding format.and -s txt will report an error.

Enjoy it! 
