import mysql.connector
import time

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='test')
print(cnx)
cursor = cnx.cursor()
firstChapter_url = ('/b/256910/123311.html', '/b/250197/')

description = ('蓝龙之工业帝国简介：    　　在赫尔塔沙漠的一个龙巢内，两条蓝龙破壳而出，一条名叫萨尔，另一条名叫莉尔娜，通过龙之传承，他们原本以为要像普通蓝龙一样，过完三千年的寿后就去见提亚马特，结果却双双觉醒了特殊血脉。于是有着异世界记忆的两条蓝龙决定弄点不一样的，他们要像蝴蝶一样煽动一下翅膀，看能否引起一场大的风暴！', '/b/250197/')
time.sleep(20)

# add_description = """insert into book (firstChapter_url) value (%s) """
update_description = """UPDATE book SET description = %s WHERE detail_url = %s"""
update_firstChapter_url = """UPDATE book SET firstChapter_url = %s WHERE detail_url = %s"""

cursor.execute(update_description, description)
cursor.execute(update_firstChapter_url, firstChapter_url)
cnx.commit()

# cursor.execute("SELECT * FROM book")
#
# myresult = cursor.fetchall()
# print(myresult)

cursor.close()
cnx.close()
