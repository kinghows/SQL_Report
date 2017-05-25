# SQL_Report
Export SQL to HTML report.  

Need install prettytable:

pip install prettytable

MySQL need install mysql-python:

pip install mysql-python

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

python sql_report.py -p dbset.ini -s html >my_report.html

use crontab regularly perform sql_report.sh

If your report results are in other languages, modify the cursor.execute('SET NAMES GBK') as the appropriate encoding format.and -s txt will report an error.

Enjoy it! 
