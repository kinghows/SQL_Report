#!/usr/local/bin/python
# coding: utf-8

# SQL Report V1.1.5
# Export SQL to HTML report,export SQL to txt file.
# Copyright (C) 2017-2017 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/SQL_Report

import getopt
import sys
import ConfigParser
import time

def f_get_conn(dbinfo,database_type):
    if database_type == "MySQL":
        try:
            conn = MySQLdb.connect(host=dbinfo[0], user=dbinfo[1], passwd=dbinfo[2], port=int(dbinfo[3]))
            return conn
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
    elif database_type == "Oracle":
        try:
            conn = cx_Oracle.connect(dbinfo[1], dbinfo[2], dbinfo[0]+':'+dbinfo[3]+'/'+dbinfo[4])
            return conn
        except cx_Oracle.DatabaseError as msg:
            print(msg)
            sys.exit(1)

def f_get_query_record(conn, query,database_type):
    cursor = conn.cursor()
    if database_type == "MySQL":
        cursor.execute('SET NAMES GBK')
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    return records

def f_print_table_txt(rows, title, style,save_as):
    field_names = []
    begin_time=time.time()
    print (title+' export to '+save_as).ljust(25,"."),
    f = open(title + '.'+save_as, 'w')
    for k in style.keys():
        field_names.append(style[k].split(',')[0])
    s = (',').join(field_names)+'\n'
    f.write(s)
    for row in rows:
        strrow=[]
        for col in row:
            strrow.append(str(col))
        s = (',').join(strrow)+'\n'
        f.write(s)
    f.close()
    exe_time=time.time()-begin_time
    print (' export OK! '+str(exe_time) +' S').rjust(50,".")

def f_print_table_xls(query,conn,title,style):
    import pandas as pd
    field_names = []
    begin_time=time.time()
    print ('export to '+title + '.xlsx').ljust(25,"."),
    cursor = conn.cursor()
    df = pd.read_sql(query,conn)
    #SQL内有中文的处理方案1：
    for k in style.keys():
        field_names.append(style[k].split(',')[0].decode('GBk'))
    df.columns = field_names
    cols = df.columns
    for e in cols:
        df[e] = df[e].map(lambda x: str(x).decode("gbk").encode("raw_unicode_escape").decode(
            "raw_unicode_escape"))
    df.to_excel(title + '.xlsx')
    #SQL内有中文的处理方案2：
    #for k in style.keys():
    #    field_names.append(style[k].split(',')[0])
    #df.columns = field_names
    #df.to_csv(title + '.csv')
    #data = pd.read_csv(title + '.csv',header=None, encoding='gbk',sep=',')
    #df = pd.DataFrame(data)
    #df.to_excel(title + '.xlsx')
    exe_time=time.time()-begin_time
    print (' export OK! '+str(exe_time) +' S').rjust(50,".")

def f_print_table_html(rows, title, style):
    print """<p /><h3 class="awr"><a class="awr" name="99999"></a>""" + title + "</h3><p />"
    print """<table border="1">"""

    print """<tr>""",
    for k in style.keys():
        print """<th class="awrbg">""",
        print style[k].split(',')[0],
        print """</th>""",
    print """</tr>"""

    linenum = 0
    for row in rows:
        k = 0
        linenum += 1
        print "<tr>",
        if linenum % 2 == 0:
            classs='awrc'
        else:
            classs='awrnc'

        for col in row:
            k += 1
            if style[k].split(',')[1] == 'r':
                print """<td align="right" class='"""+classs+"'>"+str(col)+"</td>",
            else:
                print """<td class='"""+classs+"'>"+str(col)+"</td>",
        print "</tr>"
    print """</table>
<br /><a class="awr" href="#top">Back to Top</a>
<p />
<p />
        """

def f_print_query_table(conn, title, query, style,save_as,database_type):
    rows = f_get_query_record(conn, query,database_type)
    if save_as == "html":
        f_print_table_html(rows, title, style)
    elif save_as == "txt" or save_as == "csv":
        f_print_table_txt(rows, title, style,save_as)
    elif save_as == "xls":
        f_print_table_xls(query,conn,title,style)

def f_print_caption(report_title,save_as):
    if save_as == "html":
        print """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html" />
<title>Generate by SQL_Report V1.1.5 https://github.com/kinghows/SQL_Report </title>
<style type=\"text/css\">
body.awr {font:bold 12pt Arial,Helvetica,Geneva,sans-serif;color:black; background:White;}
pre.awr  {font:12pt Courier;color:black; background:White;}
h1.awr   {font:bold 20pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;border-bottom:1px solid #cccc99;margin-top:0pt; margin-bottom:0pt;padding:0px 0px 0px 0px;}
h2.awr   {font:bold 112pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
h3.awr {font:bold 16pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
li.awr {font: 12pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
th.awrnobg {font:bold 12pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;padding-left:4px; padding-right:4px;padding-bottom:2px}
th.awrbg {font:bold 12pt Arial,Helvetica,Geneva,sans-serif; color:White; background:#0066CC;padding-left:4px; padding-right:4px;padding-bottom:2px}
td.awrnc {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;}
td.awrc    {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;}
td.awrnclb {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;}
td.awrncbb {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;border-right: thin solid black;}
td.awrncrb {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-right: thin solid black;}
td.awrcrb    {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-right: thin solid black;}
td.awrclb    {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-left: thin solid black;}
td.awrcbb    {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-left: thin solid black;border-right: thin solid black;}
a.awr {font:bold 12pt Arial,Helvetica,sans-serif;color:#663300; vertical-align:top;margin-top:0pt; margin-bottom:0pt;}
td.awrnct {font:12pt Arial,Helvetica,Geneva,sans-serif;border-top: thin solid black;color:black;background:White;vertical-align:top;}
td.awrct   {font:12pt Arial,Helvetica,Geneva,sans-serif;border-top: thin solid black;color:black;background:#FFFFCC; vertical-align:top;}
td.awrnclbt  {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-top: thin solid black;border-left: thin solid black;}
td.awrncbbt  {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;border-right: thin solid black;border-top: thin solid black;}
td.awrncrbt {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-top: thin solid black;border-right: thin solid black;}
td.awrcrbt     {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-right: thin solid black;}
td.awrclbt     {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-left: thin solid black;}
td.awrcbbt   {font:12pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-left: thin solid black;border-right: thin solid black;}
table.tdiff {  border_collapse: collapse; }
</style></head><body class="awr">
<h1 class="awr">
       """
        print report_title
        print "</h1>"
    else:
        print report_title + " begin export to "+save_as

def f_print_ending(save_as):
    if save_as == "html":
        print "<p />End of report</body></html>"
    else:
        print 'Export complete!'
        print 'Generate by SQL_Report V1.1.5'
        print 'https://github.com/kinghows/SQL_Report'

if __name__=="__main__":
    dbinfo=["127.0.0.1","root","",3306,"orcl"] #host,user,passwd,port,sid
    config_file="dbset.ini"
    report_title=""
    report_count = 0
    save_as = "html"
    database_type = "MySQL"

    opts, args = getopt.getopt(sys.argv[1:], "p:s:")
    for o,v in opts:
        if o == "-p":
            config_file = v
        elif o == "-s":
            save_as = v

    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file,"rb"))
    config.readfp(open(config_file,"rb"))
    dbinfo[0] = config.get("database","host")
    dbinfo[1] = config.get("database","user")
    dbinfo[2] = config.get("database","passwd")
    dbinfo[3] = config.get("database", "port")
    report_title = config.get("report", "report_title")
    report_count = int(config.get("report", "report_count"))
    database_type = config.get("database", "type")

    if database_type == "MySQL":
        import MySQLdb
        from warnings import filterwarnings
        filterwarnings('ignore', category=MySQLdb.Warning)
    elif database_type == "Oracle":
        import cx_Oracle
        dbinfo[4] = config.get("database", "sid")

    f_print_caption(report_title,save_as)
    conn = f_get_conn(dbinfo,database_type)

    n = 1
    while n <= report_count:
        title = config.get ( "report", "title"+str(n))
        query = config.get ( "report", "query"+str(n))
        strstyle = config.get ( "report", "style"+str(n))
        style = eval(strstyle)
        f_print_query_table(conn, title, query, style,save_as,database_type)
        n += 1

    conn.close()
    f_print_ending(save_as)