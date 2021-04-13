# SQL_Report
Export SQL to HTML report,export SQL to txt/csv/xls file.

MySQL need install 

2.7：

pip install mysql-python

3.8:

pip install mysqlclient

Oracle  need install cx_Oracle

pip install cx_Oracle

Save as xlsx need install pandas,openpyxl:

easy_install openpyxl

pip install pandas

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

2.7:

python sql_report.py >my_report.html

python sql_report.py -p dbset.ini >my_report.html

python sql_report.py -p dbset.ini -s html >my_report.html

python sql_report.py -p dbset.ini -s txt

python sql_report.py -p dbset.ini -s csv

python sql_report.py -p dbset.ini -s xls

send email:

python SendEmail.py -p emailset.ini -f my_report1.html,my_report2.html

3.8:

python3 sql_report3.py >my_report.html

python3 SendEmail3.py -p emailset.ini -f my_report1.html,my_report2.html

use crontab regularly perform sql_report.sh,auto generate  report,and send email.

If your mysql report results are in other languages, modify the cursor.execute('SET NAMES GBK') as the appropriate encoding format.

Enjoy it! 

## 好用的DBA系列，喜欢的打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)

- [Linux_Report：自定义Linux 命令生成HTML报告](https://github.com/kinghows/Linux_Report)
