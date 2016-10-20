#!/usr/bin/env python3
# _*_ conding: utf-8 _*_

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='python',
                       charset='utf8')
cur = conn.cursor()
sql = "SELECT * FROM news WHERE id =1"
cur.execute(sql)
print(cur.fetchone())
cur.close()
conn.close()
