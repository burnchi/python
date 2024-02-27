
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='kklibrary')
cursor = cnx.cursor()

tb_name = "books"
file_name = "urlQuery.txt"

cursor.execute(f"SELECT bookId FROM {tb_name}")

result = cursor.fetchall()


# root_dir = '/home/burnchi/Pictures/novelfengmian'
# root_dir1 = '/home/burnchi/Pictures/'

for i in result:
    book_url = i[0]
    with open(file_name, 'a') as f:
        f.write("https://www.uukanshu.net/b/" + book_url+'\r\n')


cursor.close()
cnx.close()
